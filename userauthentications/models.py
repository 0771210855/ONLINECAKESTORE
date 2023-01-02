from django.contrib.auth.models import AbstractUser,User
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_Admin = models.BooleanField(default=False)

class Seller(models.Model):
    SINGLESELLER = 'SELLER'
    COMPANY = 'COMPANY'
    register_as_choice = [
        (SINGLESELLER, 'singleseller'),
        (COMPANY, 'company'),
    ]
        # authetication details and privacy policy agreament
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    register_as = models.CharField(max_length=7,choices=register_as_choice,default=COMPANY)
    brand_name = models.CharField(max_length=20,db_index=True)
    
    # contact details
    phone = models.CharField(max_length=12)

    # locations
    country = models.CharField(max_length=20,db_index=True)
    district = models.CharField(max_length=20,db_index=True)
    division = models.CharField(max_length=20,db_index=True) #county / division
    parish = models.CharField(max_length=20,db_index=True) #parish / subcounty
    village = models.CharField(max_length=20,db_index=True) #village / cell
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=20,db_index=True)
    phone = models.CharField(max_length=20,db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20,db_index=True)
    email = models.EmailField()