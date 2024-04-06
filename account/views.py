from django.shortcuts import render , get_object_or_404 , redirect  
from  django.views.generic import CreateView , FormView
from django.utils.encoding import force_str , force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from hitstore1.settings import EMAIL_HOST_USER
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       LoginView)
# from django.http import HttpResponse
from .tokens import account_activation_token
from django.contrib import messages
from .models import *
from .forms import *

def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = CustomUser.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('/login/')
    else:
        messages.error(request, 'Your session is expired')

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = '/login/'

    def dispatch(self,request , *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView , self).dispatch(request , *args , **kwargs)
    
    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.is_active = False
        form.instance.save()

        subject = 'Activate your account'
        current_site = get_current_site(self.request)
        message = render_to_string('email/confirmation_email.html' , {
            'user' : form.instance,
            'domain' : current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(form.instance.pk)),
            'token': account_activation_token.make_token(form.instance) ,
        })
                
        from_email = EMAIL_HOST_USER
        to_email = self.request.POST['email']
        send_mail(
            subject,
            message,
            from_email,
            [to_email,]
        )
        messages.success(self.request , ('Please confirm your email to complete registeration.'))
        return redirect('login')



class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    authentication_form = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

        return redirect('/')

