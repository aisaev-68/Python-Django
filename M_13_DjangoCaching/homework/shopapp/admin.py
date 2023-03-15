from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.utils.formats import date_format
from .models import Product, Order, Category, Catalog, OrderItem
from .admin_mixins import ExportAsCSVMixin

# class CategoryInline(admin.TabularInline):
#     model = Category.catalog.through

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 5
    # fields = ["product", "price", "quantity"]



@admin.action(description=_("Archive products"))
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description=_("Unarchive products"))
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'tag', 'slug']
    prepopulated_fields = {'slug': ('tag',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    # inlines = [
    #     CategoryInline,
    # ]

    list_display = ["pk", "name", "category", "description_short", "slug", "attributes", "rating", "created_by", "format_date", "price",
        "discount", "image", "products_count", "sold", "archived", "brand"]
    list_display_links = "pk", "name"
    ordering = "name", "price"
    search_fields = "name",
    fieldsets = [
        (None, {
            "fields": ("category", "name", "description", "slug", "attributes", "rating", "created_by", "products_count", "sold", "image", "brand"),
        }),
        (_("Price options"), {
            "fields": ("price", "discount"),
            "classes": ("wide", "collapse"),
        }),
        (_("Extra options"), {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": _("Extra options. Field 'archived' is for soft delete"),
        })
    ]
    prepopulated_fields = {'slug': ('name',)}

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

    description_short.short_description = _("description")

    def format_date(self, obj: Product):
        return date_format(obj.created_at, "SHORT_DATETIME_FORMAT", '%Y-%m-%d %H:%M:%S')

    format_date.short_description = _("created_at")



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "product", "price", "quantity",



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]
    list_display = "delivery_address", "promocode", "format_date", "user_verbose", "paid"

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

    user_verbose.short_description = _("user")

    def format_date(self, obj: Order):
        return date_format(obj.created_at, "SHORT_DATETIME_FORMAT", '%Y-%m-%d %H:%M:%S')

    format_date.short_description = _("created_at")
