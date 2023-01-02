from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Seller,Customer,Admin,User
from django.db import transaction


# seller Registration
class seller_registration_form(UserCreationForm):
    register_as = forms.ChoiceField(choices=(('SINGLESELLER', 'Single seller'), ('COMPANY', 'under company')), label=("Group name"))
    brand_name  = forms.CharField(required=True)
    phone       = forms.CharField(required=True)
    country     = forms.CharField(required=True)
    district    = forms.CharField(required=True)
    division    = forms.CharField(required=True)
    parish      = forms.CharField(required=True)
    village     = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User  

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user) 
        seller.register_as = self.cleaned_data.get('register_as')   
        seller.brand_name  = self.cleaned_data.get('brand_name')   
        seller.phone       = self.cleaned_data.get('phone')   
        seller.country     = self.cleaned_data.get('country')   
        seller.division    = self.cleaned_data.get('division')   
        seller.parish      = self.cleaned_data.get('parish')   
        seller.village     = self.cleaned_data.get('village')   
        seller.save()
        return user       






class customer_registration_form(UserCreationForm):
    location = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user) 
        customer.location = self.cleaned_data.get('location')   
        customer.phone    = self.cleaned_data.get('phone') 
        customer.save()
        return user  
    
    
        

