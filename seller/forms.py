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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder':'Highlight on the ingrdents and flavours'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type':"file", 'class':"dropify", 'data-height':"300"}),
            'available': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
            'discountoffers': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
           }