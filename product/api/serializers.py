from rest_framework import serializers
from product.models import Product, ProductVersion, Category, Manufacturer, Color, Image


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'name',
        ]


class VersionColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'id',
            'name',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'id',
            'name',
        ]


class ProductReadSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'old_price',
            'price',
            'in_sale',
        ]


class ProductVersionSerializer(serializers.ModelSerializer):
    image = ImageSerializers(many=True)
    product = ProductReadSerializers()
    color = VersionColorSerializer()
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductVersion
        fields = [
            'id',
            'product',
            'cover_image',
            'color',
            'image',
            'detail_url',
            'quantity',
        ]

    def get_detail_url(self, obj):
        return obj.get_absolute_url()


class ProductSerializer(serializers.ModelSerializer):
    product_version = ProductVersionSerializer(many=True)
    category = CategorySerializer()
    manufacturer = ManufacturerSerializer()
    detail_url = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'old_price',
            'price',
            'in_sale',
            'product_version',
            'category',
            'manufacturer',
            'detail_url',
            'total_quantity',
        ]

    def get_detail_url(self, obj):
        return obj.get_absolute_url()

    def get_total_quantity(self, obj):
        return obj.total_quantity

    def get_version(self, obj):
        return ProductVersionSerializer(many=True).data
