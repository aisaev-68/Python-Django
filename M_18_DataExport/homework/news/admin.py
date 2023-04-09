from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from news.models import News


@admin.action(description=_("Published news"))
def mark_published(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(published=True)


@admin.action(description=_("Unpublished news"))
def mark_unpublished(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(published=False)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    actions = [
        mark_published,
        mark_unpublished,
    ]
    list_display = "pk", "title", "description", "created_at", "published",
    list_display_links = "title",
    search_fields = "title", 'description',
