# Generated by Django 4.1.7 on 2023-03-02 07:11

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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('attributes', models.JSONField(blank=True, default=dict, verbose_name='Attributes')),
                ('rating', models.FloatField(blank=True, default=0.0, verbose_name='Rating')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
                ('image', models.ImageField(default='images/default_image.jpg', upload_to='images/', verbose_name='Image product')),
                ('discount', models.SmallIntegerField(default=0, verbose_name='Discount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('products_count', models.IntegerField(verbose_name='Count')),
                ('archived', models.BooleanField(default=False, verbose_name='Status')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name', 'price'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.TextField(blank=True, null=True, verbose_name='Delivery address')),
                ('promocode', models.CharField(blank=True, max_length=20, verbose_name='Promo code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create order date')),
                ('products', models.ManyToManyField(limit_choices_to={'archived': False}, related_name='orders', to='shopapp.product', verbose_name='Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
