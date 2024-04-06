from rest_framework import serializers 
from order.models import Wishlist , Basket , BasketItem
from product.api.serializers import ProductVersionSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many = True)

    class Meta:
        model = Wishlist
        fields = [
            'user' , 
            'product'
        ]

class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = [
            'user' , 
            'product',
            'quantity',
            'subtotal',
        ]

    def get_subtotal(self,obj):
        return obj.get_subtotal()

class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many = True)

    class Meta:
        model = Basket
        fields = [
            'user' , 
            'items'
        ]