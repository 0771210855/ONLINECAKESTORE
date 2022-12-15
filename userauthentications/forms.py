from django import forms
from .models import Seller,Customer,Admin


class seller_registration_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Seller        
        fields = '__all__'


class customer_registration_form(forms.ModelForm):
    class Meta:
        model = Customer
        widgets = {
        'password': forms.PasswordInput(),
    }
        fields = '__all__'
        

class admin_registration_form(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'


