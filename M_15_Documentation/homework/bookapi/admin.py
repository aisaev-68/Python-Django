from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.utils.formats import date_format
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'year_birth',]
    search_fields = "last_name",
    list_display_links = "id", "last_name"


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'isbn', 'publication_date', 'pages',)
    search_fields = "title",
    list_display_links = "id", "title"
    filter_horizontal = ('authors',)
