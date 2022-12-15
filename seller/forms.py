from django import forms
from .models import CakeProducts,CakeCategory

class CakeCategory(forms.ModelForm):
    class Meta:
        model = CakeCategory
        fields = ['name']

class add_cake_product_form(forms.ModelForm):
    class Meta:
        model = CakeProducts
        fields = ['name','category','description','price','image','available','discountoffers']