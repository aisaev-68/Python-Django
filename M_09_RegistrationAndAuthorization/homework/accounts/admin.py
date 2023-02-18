from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "user", 'country', 'postal_code', 'city', 'address', "phone"
    list_display_links = "pk", "user"
    search_fields = "user", 'city'
