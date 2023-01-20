from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('promocode', 'delivery_address', 'created_at', 'user_id')


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
