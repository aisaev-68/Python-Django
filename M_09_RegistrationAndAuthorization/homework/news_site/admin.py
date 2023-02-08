from django.contrib import admin
from .models import Profile, Article


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = "pk", "user", "phone", "city", "verification_flag", "count_news"
    list_display_links = "pk", "user"
    # ordering = "-user", "pk"
    search_fields = "user", "city"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = "pk", "title", "content", "published", "modified", "author"
    list_display_links = "pk", "author"
    ordering = "-author", "pk"
    search_fields = "author", "title"
