from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView 
from rest_framework.views import APIView
from rest_framework import permissions

from rest_framework.permissions import DjangoModelPermissions

# from rest_framework.views import APIView

from product.models import Product , ProductVersion
from .serializers import ProductSerializer , ProductVersionSerializer
from django_filters.rest_framework import DjangoFilterBackend

# import django_filters

# class ProductFilter(django_filters.FilterSet):
#     color = django_filters.CharFilter(
#         field_name='product_version__color__name',
#         lookup_expr='iexact',  # Case-insensitive exact match
#     )

#     class Meta:
#         model = Product
#         fields = ['category', 'manufacturer', 'color']


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['category' , 'manufacturer' ]

    

class ColorAPIView(ListAPIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['color']



class ProductApiView(APIView):
    serializer_class = ProductSerializer

    def get(self , request , *args , **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk = kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            all_products = Product.objects.all()
            serializer = self.serializer_class( all_products , many = True)

        return Response(serializer.data , status = status.HTTP_200_OK)
    
class ProductVersionApiView(APIView):
    queryset = ProductVersion.objects.all()
    serializer_class = ProductVersionSerializer

    def get(self , request , *args , **kwargs):
        if kwargs.get('product_id'):
            obj = ProductVersion.objects.filter(product_id = kwargs.get('product_id'))
            stat = status.HTTP_200_OK
            result = self.serializer_class(obj , many = True).data
            if kwargs.get('pk'):
                obj = ProductVersion.objects.get(pk = kwargs.get('pk'))
                result = self.serializer_class(obj).data
        else:
            stat = status.HTTP_404_NOT_FOUND
            result = {'error' : 'Product not found!'}
        return Response(result , status = stat)
    
