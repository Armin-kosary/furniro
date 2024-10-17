from django.db import models
from uuid import uuid4
# Create your models here.

class ProductTag(models.Model):
    title = models.CharField(max_length=20)

class ProductCategory(models.Model):
    title = models.CharField(max_length=20)

class ProductColor(models.Model):
    title = models.CharField(max_length=20)

class ProductSize(models.Model):
    title = models.CharField(max_length=20)

class Product(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True)
    short_description = models.TextField()
    full_description = models.TextField()
    size = models.ManyToManyField(ProductSize)
    color = models.ManyToManyField(ProductColor)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(ProductTag)
    score = models.IntegerField()
    product_code = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.product_code:
            self.product_code = uuid4()
        super(Product, self).save(*args, **kwargs)