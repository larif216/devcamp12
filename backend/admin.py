from django.contrib import admin
from .models import Category, Merk, Product, Voucher, Regional

# Register your models here.
admin.site.register(Category)
admin.site.register(Merk)
admin.site.register(Product)
admin.site.register(Voucher)
admin.site.register(Regional)
