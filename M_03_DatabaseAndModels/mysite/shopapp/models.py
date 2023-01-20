from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    discount = models.PositiveSmallIntegerField(default=0, verbose_name='Процентаная скидка')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    archived = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name='Код заказа')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name="orders")

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return 'Order {}'.format(self.promocode)
