# Generated by Django 4.1.6 on 2023-02-08 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Номер телефона')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('verification_flag', models.BooleanField(choices=[(1, 'Выберите значение'), (2, False), (3, True)], default=False, verbose_name='Статус')),
                ('count_news', models.IntegerField(default=0, verbose_name='Количество обуликованных новостей')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['user', 'city'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Статья')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'ordering': ['-published'],
                'permissions': (('change_name', 'can change name of product'),),
            },
        ),
    ]
