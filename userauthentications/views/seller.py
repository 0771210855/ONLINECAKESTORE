from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib import messages

from ..forms import seller_registration_form
# from ..models import User

def sellerSignup(request):    
    context={'form':seller_registration_form}
    if request.method == 'POST':
        form = seller_registration_form(request.POST)   
        if form.is_valid():
            form.save() 
            messages.info(request,'Product added successfully')
            return redirect('add_cake_product')    
    return render(request,'userauthentications/signup.html',context)