from django.contrib import admin
from .models import Store, Laptop, Order

admin.site.register(Store)
admin.site.register(Laptop)
admin.site.register(Order)