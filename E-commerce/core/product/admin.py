from django.contrib import admin
from .models import Product , CustomerCart , CartItem
# Register your models here.
admin.site.register(Product)
admin.site.register(CustomerCart)
admin.site.register(CartItem)