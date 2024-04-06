from django.contrib import admin
from .models import Blogs , Comment , Author , BlogType
from django.utils.html import format_html

# Register your models here.
admin.site.site_header = 'HITSTORE ADMIN'

class BlogAddVersion(admin.StackedInline):
    model = Blogs
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','types','created_time','get_file']
    list_filter = ['types','author']
    list_editable = ['types']
    search_fields = ['title','author__title']
    fieldsets = [
        ('General Info', {'fields': ('title','author')}),
        ('Detail Info', {'fields' : ('types','description','image')})
    ]


    def get_file(self, obj):
        if obj.image:
            file_extension = obj.image.name.split('.')[-1].lower()
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                img = '<img src="{url}" width="200px" />'.format(url=obj.image.url)
                return format_html(img)
            elif file_extension in ['mp4', 'webm']:
                video = '<video width="320" height="240" controls><source src="{url}" type="video/{ext}">Your browser does not support the video tag.</video>'.format(url=obj.image.url, ext=file_extension)
                return format_html(video)
            elif file_extension in ['mp3', 'ogg']:
                audio = '<audio controls><source src="{url}" type="audio/{ext}">Your browser does not support the audio tag.</audio>'.format(url=obj.image.url, ext=file_extension)
                return format_html(audio)
        return ''
    

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BlogAddVersion]




admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BlogType)