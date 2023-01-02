from django.db import models
from django.urls import reverse
from userauthentications.models import Seller
# Create your models here.

class CakeCategory(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    # slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class CakeProducts(models.Model):
    category = models.ForeignKey(CakeCategory,related_name="products",on_delete=models.CASCADE)
    name = models.CharField(max_length=200,db_index=True)
    # slug =models.SlugField(max_length=200,db_index=True)
    seller = models.ForeignKey(Seller,related_name="product_Owner",on_delete=models.CASCADE,null= True, default='1' )
    image = models.ImageField(upload_to='products/%y/%m/',blank=True)
    description =models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    discountoffers = models.BooleanField(default=False,verbose_name = "any discounts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =('name',)
        

    def __str__(self):
        return self.name
