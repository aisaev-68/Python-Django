from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Post, PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "description_short", "created_by", "created_at"
    list_display_links = "pk", "title"
    ordering = "-title", "pk"
    search_fields = "title", "description_short"

    def description_short(self, obj: Post) -> str:
        if len(obj.description) < 100:
            return obj.description
        return obj.description[:100] + "..."

@admin.register(PostImage)
class PostAdmin(admin.ModelAdmin):
    list_display = "pk", "post", "image"
    list_display_links = "pk", "post"
    ordering = "-pk", "post"
    search_fields = "image",