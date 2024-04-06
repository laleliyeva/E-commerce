from django.db import models

# Create your models here.

from hitstore1.utils.base import BaseModel


class Author(BaseModel):
    title = models.CharField(max_length=100 , verbose_name='Title of the author' , help_text='Max 100 character')
    description = models.TextField(max_length=1000 , verbose_name='Description of the author' , help_text='Max 1000 character' , blank=True , null=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.title
        

class Blogs(BaseModel):
    image = models.FileField(upload_to='blog_media' ,  verbose_name= 'Medias of the blog ' , help_text= 'Just media')
    author = models.ForeignKey('blog.Author' , on_delete=models.CASCADE , verbose_name='Author of the blog', related_name='author')
    title = models.CharField(max_length = 100 , verbose_name = 'Title of the blog',help_text = 'Max 100 character') 
    description = models.TextField(verbose_name='Descripyion of the blog ', help_text='Max 1000 character')
    types = models.ForeignKey('blog.BlogType', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
    

    
class BlogType(BaseModel):
    types = models.CharField(max_length=20 , verbose_name = 'Type of the blog')

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    
    def __str__(self):
        return self.types


class Comment(BaseModel):
    name = models.CharField(max_length=100 , verbose_name='Name of the commenter' )
    email = models.EmailField(max_length=100 , verbose_name='Email')
    title = models.CharField(max_length=100 , verbose_name='Title of the comment')
    comments = models.TextField()
    blog_id = models.ForeignKey('blog.Blogs' , on_delete=models.CASCADE , related_name='com' )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return self.title 
    
