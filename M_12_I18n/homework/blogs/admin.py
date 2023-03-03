from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.formats import date_format
from django.utils.translation import gettext_lazy as _

from .models import Post, PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "description_short", "created_by", "format_date"
    list_display_links = "pk", "title"
    ordering = "-title", "pk"
    search_fields = "title",

    def description_short(self, obj: Post) -> str:
        if len(obj.description) < 100:
            return obj.description
        return obj.description[:100] + "..."

    description_short.short_description = _("description")

    def format_date(self, obj: Post):
        return date_format(obj.created_at, "SHORT_DATETIME_FORMAT", '%Y-%m-%d %H:%M:%S')

    format_date.short_description = _("created_at")


@admin.register(PostImage)
class PostAdmin(admin.ModelAdmin):
    list_display = "pk", "post_short", "image"
    list_display_links = "pk", "post_short"
    ordering = "-pk",
    search_fields = "image",

    def post_short(self, obj: PostImage) -> str:
        if len(obj.post.description) < 40:
            return obj.post.description
        return obj.post.description[:40] + "..."

    post_short.short_description = _("post")
