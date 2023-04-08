from django.contrib import admin

from payment.models import Billing, Invoice


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = "pk", 'user', "created_at", 'replenishment_amount', "balance",
    list_display_links = "pk", "user"
    search_fields = "user",


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = "pk", 'user', "created_at", 'amount', "product"
    list_display_links = "pk", "user"
    search_fields = "user",