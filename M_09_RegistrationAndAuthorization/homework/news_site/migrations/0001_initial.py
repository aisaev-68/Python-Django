# Generated by Django 4.1.6 on 2023-02-04 15:51

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('city', models.TextField(blank=True, verbose_name='Город')),
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
    ]
