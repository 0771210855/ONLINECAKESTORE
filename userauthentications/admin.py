from django.contrib import admin

# Register your models here.


from .models import Customer, User ,Seller

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Seller)
