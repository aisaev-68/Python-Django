# Generated by Django 4.1.6 on 2023-02-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(default=0, verbose_name='Процентная скидка'),
        ),
    ]
