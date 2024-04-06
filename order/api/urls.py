from django.urls import path 
from .views import WishlistApiView , BasketApiView

urlpatterns = [
    path('api/wishlist/' , WishlistApiView.as_view() , name = 'api_wishlist'),
    path('api/basket/' , BasketApiView.as_view() , name = 'api_basket'),
]