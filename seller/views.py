from unicodedata import category
from django.shortcuts import render, redirect
from .forms import add_cake_product_form,CakeCategory
from django.contrib import messages
from .models import CakeProducts

# Create your views here.

def add_category(request):
    formdata = CakeCategory()
    if request.method == 'POST':
        formdata = CakeCategory(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('add_cake_product')

    return render(request,'seller/category.html',{'CakeCategory':CakeCategory})



def add_cake_product(request):
    form = add_cake_product_form()
    context = {'add_cake_product_form':form}
    if request.method == 'POST':
        form = add_cake_product_form(request.POST,request.FILES)   
        if form.is_valid():
            form.save() 
            messages.info(request,'Product added successfully')
    return render(request,'seller/addproduct.html',context)


def list_cake_product(request):
    cake_products = CakeProducts.objects.all()
    context = {'cake_products':cake_products}
    return render(request,'seller/viewproduct.html',context)

def edit_cake_product(request,pk):
    cake_product = CakeProducts.objects.get(id = pk)
    form = add_cake_product_form(instance=cake_product)   
  
    if request.method == "POST":  
        form = add_cake_product_form(request.POST ,request.FILES,instance = cake_product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'add_cake_product_form': form, 'cake_product': cake_product}

    return render(request, 'seller/addproduct.html', context)
