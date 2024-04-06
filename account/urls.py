from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView ,   CustomLoginView , activate 

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]