from django.shortcuts import render
from seller.models import CakeProducts

# Create your views here.
def home(request):
    product = CakeProducts.objects.all()
    return render(request,"customer/home.html",{"product":product})
