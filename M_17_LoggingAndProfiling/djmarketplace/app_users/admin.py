from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = "pk", 'avatar', "user", 'country', 'postal_code', 'city', 'address', "phone", "status"
    list_display_links = "pk", "user"
    search_fields = "user", 'city'
