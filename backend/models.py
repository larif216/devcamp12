from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Merk(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    merk_id = models.ForeignKey(Merk, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    model_time = models.DateField()

class Voucher(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    time = models.DateField()
    discount = models.IntegerField()

# class Purchase(models.Model):
#     product_id