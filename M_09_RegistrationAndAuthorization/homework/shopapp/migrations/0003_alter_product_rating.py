# Generated by Django 4.1.6 on 2023-02-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, max_length=5, verbose_name='Рейтинг'),
        ),
    ]
