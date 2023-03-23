from django.contrib import admin

from shopapp.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "address",
    list_display_links = "pk", "name"
    search_fields = "name", 'address'
