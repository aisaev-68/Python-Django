from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    CHOICE = [(1, 'Выберите значение'), (2, False), (3, True)]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles', verbose_name='Пользователь')
    country = models.CharField(max_length=100, verbose_name='Страна', blank=True)
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс', blank=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    address = models.CharField(max_length=200, verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=20, db_index=True, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["user", "address"]
