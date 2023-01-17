from django.contrib import admin
from . import models


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price')

admin.site.register(models.Product)
# admin.site.register(models.Product, ProductAdmin)
