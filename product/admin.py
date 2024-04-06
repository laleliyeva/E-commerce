from django.contrib import admin
from .models import Product , Color , Manufacturer , Category , Image , ProductVersion , ReviewComment
from django.utils.html import format_html



    
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(ProductVersion)
admin.site.register(ReviewComment)