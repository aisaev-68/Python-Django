from django.db import models


class Files(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    uploadedFile = models.FileField(blank=True, null=True, unique=True, verbose_name='Файл')
    dateTimeOfUpload = models.DateTimeField(auto_now=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.uploadedFile.name
