# Generated by Django 4.1.6 on 2023-02-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0, max_length=5, null=True, verbose_name='Рейтинг'),
        ),
    ]