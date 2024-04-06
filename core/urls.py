from django.urls import path
from .views import  SearchView , IndexView

urlpatterns = [
    path('search/' , SearchView.as_view() , name =  'search'),
    path('' , IndexView.as_view() , name =  'index'),
    # path('about-us/' , about_us , name =  'about'),
    # path('contact-us/' , contact_us , name =  'contact'),
    # path('faq/' , faq , name =  'faq'),

]




