from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
# admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderltem)
admin.site.register(ShippingAddress)