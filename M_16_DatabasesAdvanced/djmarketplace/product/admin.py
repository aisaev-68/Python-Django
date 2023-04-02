from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.formats import date_format
from django.utils.translation import gettext_lazy as _

from product.admin_mixins import ExportAsCSVMixin
from product.models import Product, ShopItem
from shopapp.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = "pk", "shop_name", "address",
    list_display_links = "pk", "shop_name"
    search_fields = "shop_name", 'address'

class ShopItemInline(admin.TabularInline):
    model = ShopItem
    extra = 5


@admin.action(description=_("Archive products"))
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description=_("Unarchive products"))
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        ShopItemInline,
    ]


    list_display = ["pk", "name", "description_short", "attributes", "rating", "created_by", "format_date", "price", "new_price",
        "discount", "image", "products_count", "sold", "archived", "brand"]
    list_display_links = "pk", "name"
    ordering = "name", "new_price"
    search_fields = "name",
    fieldsets = [
        (None, {
            "fields": ("name", "description", "attributes", "rating", "created_by", "products_count", "sold", "image", "brand"),
        }),
        (_("Price options"), {
            "fields": ("price", "new_price", "discount"),
            "classes": ("wide", "collapse"),
        }),
        (_("Extra options"), {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": _("Extra options. Field 'archived' is for soft delete"),
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

    description_short.short_description = _("description")

    def format_date(self, obj: Product):
        return date_format(obj.created_at, "SHORT_DATETIME_FORMAT", '%Y-%m-%d %H:%M:%S')

    format_date.short_description = _("created_at")





@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ["pk", "shop", "product",]
    list_display_links = "pk", "shop"
    ordering = "shop", "product"
    search_fields = "shop",
    # inlines = [
    #     ShopItemInline,
    # ]