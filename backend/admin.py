from django.contrib import admin
from .models import Category, Merk, Product, PlannedVoucher, Regional, Purchase

# Register your models here.
admin.site.register(Category)
admin.site.register(Merk)
admin.site.register(Product)
admin.site.register(PlannedVoucher)
admin.site.register(Regional)
admin.site.register(Purchase)
