from django.urls import path
from .views import seller ,customer


app_name = 'userauthentication'

urlpatterns=[
    path('',seller.sellerSignup,name='sellersignup'),
    path('customer/',customer.customerSignup,name='customersignup'),
]