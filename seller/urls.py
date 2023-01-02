from django.urls import path
from . import views


app_name = 'seller'

urlpatterns=[
    path('',views.seller_home,name='seller_home'),
    path('addcategory',views.add_category,name='add_cake_category'),
    path('addproduct',views.add_cake_product,name='add_cake_product'),
    path('viewproducts',views.list_cake_product,name='view_products'),
    path('editproduct/<str:pk>',views.edit_cake_product,name='edit_product'),
]