from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPES = [("Canastilla", "Juguetes", "Hogar")]
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE())
    precio = models.IntegerField()
    amounts_begin = models.IntegerField()
    amounts = models.IntegerField()
    supplier = models.CharField(max_length=100, choices=PRODUCT_TYPES, default=None, null=True)


class ProductHistory(models.Model):
    amount=models.IntegerField()
    product_id=models.ForeignKey()
    sold_by=models.CharField(max_length=250,null=True)
    create_at=models.DateTimeField(default=timezone.now())