from django.contrib import admin
from . import models


@admin.register(models.Files)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'uploadedFile', 'dateTimeOfUpload')
    search_fields = "title",
    ordering = 'pk',
