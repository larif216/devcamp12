from django.contrib import admin
from .models import Category, Merk, Product, Voucher

# Register your models here.
admin.site.register(Category)
admin.site.register(Merk)
admin.site.register(Product)
admin.site.register(Voucher)
