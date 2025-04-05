from django.contrib import admin
from .models import Store, Laptop, Order

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store', 'stock')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('laptop', 'quantity', 'store', 'created_at')