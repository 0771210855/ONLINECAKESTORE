from django.urls import path
from .views import seller ,customer


app_name = 'userauthentication'

urlpatterns=[
    path('seller-signup/',seller.sellerSignup.as_view(),name='seller_signup'),

    path('seller-signin/',seller.sellerSignin,name='seller_signin'),

    path('logout-seller/',seller.logout_request,name="seller_logout"),

    path('customer-signup/',customer.customerSignup.as_view(),name='customer_signup'),
    
    path('customer-signin/',customer.customerSignin,name='customer_signin'),

    path('logout-customer/',customer.logout_request,name="customer_logout"),
]