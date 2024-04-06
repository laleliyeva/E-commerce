from django.urls import path ,  include
from .views import ProductListView , ColorAPIView , ProductApiView , ProductVersionApiView

product_patterns = [
    path('api/products/' , ProductListView.as_view() , name = 'products'), 
    path('api/product_color/' , ColorAPIView.as_view() , name = 'product_color'), 
    path('api/products/<int:pk>/' , ProductApiView.as_view() , name = 'api_product'), 
    path('api/products/<product_id>/versions/' , ProductVersionApiView.as_view() , name = 'product_versions'), 
    path('api/products/<product_id>/versions/<int:pk>/' , ProductVersionApiView.as_view() , name = 'product_version'), 



]


urlpatterns = [
    # path('api/version/',ColorAPIView.as_view(),name='version'),
    path('', include(product_patterns))
]
