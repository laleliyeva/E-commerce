from django.urls import path
from .views import ProductListView , ProductDetailView

urlpatterns = [
    path('shop/' , ProductListView.as_view() , name =  'shop'),
    path('single-product/<int:pk>/' , ProductDetailView.as_view() , name = 'product'),
]