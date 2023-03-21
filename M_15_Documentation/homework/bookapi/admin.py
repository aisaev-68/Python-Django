from django.contrib import admin
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
