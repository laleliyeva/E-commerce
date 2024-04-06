from django import forms 
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email' , )
        widgets = {
            'email' : forms.EmailInput(attrs={'class' : 'input-text required-entry validate-email' , 'placeholder': 'Enter your email!'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email = email).exists():
            raise forms.ValidationError('Email already in use')
        return email