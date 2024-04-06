from django.db import models
from django.urls import reverse
from hitstore1.utils.base import BaseModel

    
class Color(BaseModel):
    name = models.CharField(max_length=20 , verbose_name= 'Color of the product')

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name

class Image(BaseModel):
    name = models.ImageField(upload_to='product')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.id}'

class Manufacturer(BaseModel):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(BaseModel):
    name = models.CharField(max_length = 100 , verbose_name = 'Name of the product',help_text = 'Max 100 character')
    old_price = models.PositiveIntegerField(blank=True , null=True)
    price = models.IntegerField(verbose_name='Price of the product')
    in_sale = models.BooleanField(default = False)
    manufacturer = models.ForeignKey('product.Manufacturer' , on_delete=models.CASCADE)
    category = models.ForeignKey('product.Category' , on_delete=models.CASCADE)
    description = models.TextField()


    @property 
    def total_quantity(self):
        return sum(versions.quantity for versions in self.product_version.all())


    @property
    def get_version(self):
        for version in self.product_version.all():
            return version.pk
        
    def get_absolute_url(self):
        return reverse('product', kwargs={"pk": self.get_version})
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class ProductVersion(BaseModel):
    product = models.ForeignKey('product.Product' , on_delete=models.CASCADE , related_name = 'product_version')
    color = models.ForeignKey('product.Color' , on_delete=models.CASCADE , related_name= 'product_version_color')
    cover_image = models.ImageField(upload_to='product')
    image = models.ManyToManyField('product.Image' )
    quantity = models.IntegerField(verbose_name='Quantity of the product' , blank = True , null = True , default = 0)



    def get_absolute_url(self):
        return reverse('product', kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Product Verion'
        verbose_name_plural = 'Product Versions'

    def __str__(self):
        return f"{self.product.name}'s {self.color.name} version"
    

class ReviewComment(BaseModel):
    
    quality = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    value = models.PositiveBigIntegerField()

    nickname = models.CharField(max_length=100 , verbose_name='Nickname' )
    summary = models.CharField(max_length=100 , verbose_name='Nickname' )
    review =  models.TextField()
    key = models.ForeignKey('product.Product' ,on_delete=models.CASCADE , related_name= 'product_review')


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.nickname 
    

    