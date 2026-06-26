from django.contrib import admin
from . import models
from .models import Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'is_active']
    list_editable = ['price', ]
    list_filter = ['category']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductTag)
# admin.site.register(models.ProductBrand)
admin.site.register(models.ProductModel)
admin.site.register(models.Instructor)
admin.site.register(Category)


# Register your models here.
