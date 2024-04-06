from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from .models import ProductVersion
from .forms import *
from  django.views.generic import ListView , DetailView, CreateView


class ProductListView(ListView):
    model = Product
    template_name = 'shop.html'
    paginate_by = 4
    context_object_name = 'products'


    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manu'] = Manufacturer.objects.all()
        context['color'] = Color.objects.all()
        context['category'] = Category.objects.all()
        return context


class ProductDetailView(DetailView, CreateView):
    model = Product
    template_name = 'single-product.html'
    context_object_name = 'product'
    form_class = ReviewForm


    def get_object(self):
        return ProductVersion.objects.filter(pk = self.kwargs['pk']).first()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_colors = []
        product = Product.objects.get(product_version=self.get_object())
        versions = product.product_version.all()
        related_product=Product.objects.filter(category=product.category).exclude(product_version=self.get_object())

        for version in versions:
            product_colors.append({'id': version.id , 'product': version.product.id , 'color': version.color})


        context['colors'] = product_colors
        context['images'] = self.get_object().image.all()
        context['related']=related_product
        return context
    

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.key = Product.objects.get(product_version=self.get_object())
            comment.save()
        return redirect('product' , pk=self.kwargs.get('pk') )