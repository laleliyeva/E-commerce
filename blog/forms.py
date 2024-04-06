from django import forms
from .models import *

# from django.forms import widgets


class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('blog_id',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name' , 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email' , 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholde': 'Title of the comment', 'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'})
            }
        