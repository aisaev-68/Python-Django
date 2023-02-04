from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = "pk", "user", "phone", "city", "verification_flag", "count_news"
    list_display_links = "pk", "user"
    ordering = "-user", "pk"
    search_fields = "user", "description"
