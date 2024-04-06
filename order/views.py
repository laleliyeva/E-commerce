from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import *


class BasketView(LoginRequiredMixin,ListView):
    model = Basket
    template_name = 'basket.html'
    context_object_name = 'basket'

    def get_queryset(self):
        return Basket.objects.filter(user = self.request.user).first()

class WishlistView(LoginRequiredMixin,ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    context_object_name = 'wishlist'

    def get_queryset(self):
        return Wishlist.objects.filter(user = self.request.user).first()
    
