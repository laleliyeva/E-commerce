# from rest_framework import serializers 
from order.models import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView 
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import WishlistSerializer , BasketSerializer
from product.models import ProductVersion

# from rest_framework.permissions import DjangoModelPermissions

# from rest_framework.views import APIView

from product.models import Product , ProductVersion
from django_filters.rest_framework import DjangoFilterBackend

class WishlistApiView(APIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    http_method_names = ['get' , 'post' , 'delete']

    def get(self , request , *args , **kwargs):
        wishlist = Wishlist.objects.filter(user = self.request.user).first()
        serializer = self.serializer_class(wishlist)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def post(self , request , *args , **kwargs ):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(id = product).first()
        if version and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user = self.request.user).first()
            if wishlist:
                wishlist.product.add(version)
            else:
                wishlist = Wishlist.objects.create(user = self.request.user)
                wishlist.product.add(version)
            serializer = self.serializer_class(wishlist)
            return Response(serializer.data , status=status.HTTP_201_CREATED)

    def delete(self , request , *args , **kwargs ):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(id = product).first()
        if version and self.request.user.is_authenticated:
            wishlist = Wishlist.objects.filter(user = self.request.user).first()
            if wishlist:
                wishlist.product.remove(version)
                serializer = self.serializer_class(wishlist)
                return Response(serializer.data , status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            


class BasketApiView(APIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    http_method_names = ['get' , 'post' , 'delete']

    def get(self , request , *args , **kwargs):
        basket = Basket.objects.filter(user = self.request.user).first()
        serializer = self.serializer_class(basket)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request , *args , **kwargs ):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(id = product).first()
        quantity = request.data.get('quantity')

        if version and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user = self.request.user).first()
            if basket:
                basket_item = basket.items.filter(product = version).first()
                if basket_item:
                    basket_item.quantity += 1
                    basket_item.save()
                else:
                    basket_item = basket.items.create(user = self.request.user , product = version , quantity = quantity)
            else:
                basket = Basket.objects.create(user = self.request.user)
                basket_item = basket.items.create(user = self.request.user , product = version , quantity = quantity)
            serializer = self.serializer_class(basket)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
    def delete(self , request , *args , **kwargs ):
        product = request.data.get('product')
        version = ProductVersion.objects.filter(id = product).first()
        if version and self.request.user.is_authenticated:
            basket = Basket.objects.filter(user = self.request.user).first()
            if basket:
                basket_item = basket.items.filter(product = version).first()
                if basket_item:
                    basket_item.delete()
                    return Response( status=status.HTTP_200_OK)
                else:
                    return Response( status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)