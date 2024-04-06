from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import *
from  django.views.generic import ListView , DetailView

class BlogListView(ListView):
    model = Blogs
    template_name = 'blog.html'
    context_object_name = 'allblogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        author_id = self.request.GET.get('author_id')
        type_id = self.request.GET.get('type_id') 
        
        if author_id:
            queryset = queryset.filter(author_id=author_id).all()
        
        elif type_id:
            queryset = queryset.filter(types_id=type_id).all()


        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['blog_types'] = BlogType.objects.all()
        context['recent'] = Blogs.objects.order_by('-created_time')[:5]
        
        return context


class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogForm()
        context['authors'] = Author.objects.all()
        context['blog_types'] = BlogType.objects.all()
        context['recent'] = Blogs.objects.order_by('-created_time')[:5]
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        blogform = BlogForm(request.POST)
        if blogform.is_valid():
            comment = blogform.save(commit=False)
            comment.blog_id = self.object
            comment.save()
        return self.render_to_response(self.get_context_data(form=blogform))