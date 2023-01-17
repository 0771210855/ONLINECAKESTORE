from unicodedata import category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import add_cake_product_form,CakeCategory
from django.contrib import messages
from .models import CakeProducts
from userauthentications.models import Seller

# Create your views here.




@login_required(login_url='auth:seller_signin')
def seller_home(request):
    user_id = request.user.id
    # seller = Seller.objects.get(user_id = user_id)    
    return render(request,'seller/index.html',)


@login_required(login_url='auth:seller_signin')
def add_category(request):
    formdata = CakeCategory()
    if request.method == 'POST':
        formdata = CakeCategory(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('seller:add_cake_product')

    return render(request,'seller/category.html',{'CakeCategory':CakeCategory})


@login_required(login_url='auth:seller_signin')
def add_cake_product(request):
    form = add_cake_product_form()
    context = {'add_cake_product_form':form}
    if request.method == 'POST':
        form = add_cake_product_form(request.POST,request.FILES)
        if form.is_valid():
            add_owner = form.save(commit=False)
            add_owner.product_owner = request.user
            add_owner.save()
            messages.info(request,'Product added successfully')
    return render(request,'seller/addproduct.html',context)

@login_required(login_url='auth:seller_signin')
def list_cake_product(request):
    cake_products = CakeProducts.objects.filter(product_owner_id = request.user)
    context = {'cake_products':cake_products}
    return render(request,'seller/viewproduct.html',context)

@login_required(login_url='auth:seller_signin')
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
