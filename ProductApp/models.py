from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=60)
    text = models.TextField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

# Create your models here.
