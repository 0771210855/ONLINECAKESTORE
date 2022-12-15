from django.urls import path
from . import views


app_name = 'seller'

urlpatterns=[
    path('',views.add_cake_product,name='add_cake_product'),
    path('addcategory',views.add_category,name='add_cake_category'),
    path('viewproducts',views.list_cake_product,name='viewproducts'),
    path('editproduct/<str:pk>',views.edit_cake_product,name='editproduct'),
]