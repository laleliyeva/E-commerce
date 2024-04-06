from django.urls import path
from .views import  WishlistView , BasketView

urlpatterns = [
    # path('checkout/' , checkout , name =  'checkout'),
    path('basket/' , BasketView.as_view() , name = 'basket'),
    path('wishlist/' , WishlistView.as_view() , name = 'wishlist'),
]