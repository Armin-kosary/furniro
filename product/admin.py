from django.contrib import admin
from .models import Product, ProductCategory, ProductColor, ProductSize, ProductTag
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductCategory)