from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    CHOICE = [(1, False), (2, True)]
    class Meta:
        ordering = ["name", "price"]
        # db_table = "tech_products"
        # verbose_name_plural = "products"

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Цена')
    discount = models.SmallIntegerField(default=0, verbose_name='Процентаная скидка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    archived = models.BooleanField(choices=CHOICE, default=False, verbose_name='Статус')

    @property
    def description_short(self):
        if len(self.description) < 50:
            return self.description
        return self.description[:48] + "..."

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name='Промокод')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, related_name="orders")
