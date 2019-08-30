from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Merk(models.Model):
    name = models.CharField(max_length=50)

class Regional(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    merk_id = models.ForeignKey(Merk, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    model_time = models.DateField(null=True)

class PlannedVoucher(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    regional_id = models.ForeignKey(Regional, on_delete=models.CASCADE)
    time = models.DateField()
    voucher_discount = models.IntegerField()
    voucher_count = models.IntegerField()

class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    merk_id = models.ForeignKey(Merk, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    regional_id = models.ForeignKey(Regional, on_delete=models.CASCADE)
    time = models.DateField()
    voucher_discount = models.IntegerField()
    voucher_count = models.IntegerField()
    count = models.IntegerField(default=0)
