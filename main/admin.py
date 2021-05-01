from django.contrib import admin
from .models import OrderList, Order, Cocktail

# Register your models here.
admin.site.register(OrderList)
admin.site.register(Order)
admin.site.register(Cocktail)
