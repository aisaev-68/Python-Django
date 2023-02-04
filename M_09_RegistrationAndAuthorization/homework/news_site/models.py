from time import timezone

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    CHOICE = [(1, 'Выберите значение'), (2, False), (3, True)]

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["user", "city"]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=100,verbose_name='Город', blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    verification_flag = models.BooleanField(choices=CHOICE, default=False, verbose_name='Статус')
    count_news = models.IntegerField(default=0, verbose_name='Количество обуликованных новостей')


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Статья', blank=True)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    modified = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Статьи"
        ordering = ['-published']