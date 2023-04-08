from django.contrib import admin
from django.utils.formats import date_format
from django.utils.translation import gettext_lazy as _

from order.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 5


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "product", "total_price", "quantity",


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
