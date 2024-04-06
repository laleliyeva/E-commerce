from django.db import models
from account.models import CustomUser
from product.models import ProductVersion

# Create your models here.
class Wishlist(models.Model):
    user = models.OneToOneField('account.CustomUser', on_delete=models.CASCADE , related_name='user_wishlist')
    product = models.ManyToManyField('product.ProductVersion' , related_name='product_wishlist')

    def __str__(self):
        return f"{self.user.email}'s wishlist"
    
    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

class BasketItem(models.Model):
    user = models.ForeignKey('account.CustomUser' , on_delete=models.CASCADE , related_name='user_basket_item')
    product = models.ForeignKey('product.ProductVersion' , on_delete=models.CASCADE , related_name='product_basket_item')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.email}'s basket item"
    
    def get_subtotal(self):
        return self.product.product.price * self.quantity
    
    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'

class Basket(models.Model):
    user = models.OneToOneField('account.CustomUser' , on_delete=models.CASCADE , related_name='user_basket')
    items = models.ManyToManyField('order.BasketItem' ,  related_name='basket_item')

    def __str__(self):
        return f"{self.user.email}'s basket"
    
    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'