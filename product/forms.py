from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
        fields = '__all__'
        exclude = ('key',)
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': 'NickName' , 'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'placeholder': 'Summary' , 'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
            }