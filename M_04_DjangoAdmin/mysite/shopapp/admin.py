from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from . import models


class OrderInline(admin.TabularInline):
    model = models.Product.orders.through


class ProductInline(admin.TabularInline):
    model = models.Order.product.through


@admin.action(description="Архивация продукта")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Деархивация продукта")
def unmark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        unmark_archived,
    ]
    inlines = [
        OrderInline,
    ]
    list_display = ('pk', 'name', 'description_short', 'price', 'discount', 'archived')
    search_fields = "name", "discount"
    ordering = 'pk',
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ("Цена и скидка", {
            'fields': ('price', 'discount')
        }),
        ('Дополнительные опции', {
            'classes': ('collapse',),
            'fields': ('archived',),
        }),
    )

    def description_short(self, obj: models.Product) -> str:
        if len(obj.description) < 40:
            return obj.description
        return obj.description[:40] + "..."


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = ('pk', 'promocode', 'delivery_address', 'created_at', 'user_verbose')
    search_fields = "delivery_address", "promocode"

    def get_queryset(self, request):
        return models.Order.objects.select_related("user").prefetch_related("product").all()

    def user_verbose(self, obj: models.Order) -> str:
        return obj.user.first_name or obj.user.username
