from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True)
    attributes = models.JSONField(default=dict, blank=True, verbose_name='Атрибуты')
    created_by = models.ForeignKey(User, verbose_name='Кем создан', on_delete=models.CASCADE, null=True)
    rating = models.FloatField(verbose_name='Рейтинг', blank=True, default=0.0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение продукта',
                              default='images/default_image.jpg')
    discount = models.SmallIntegerField(default=0, verbose_name='Процентная скидка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    products_count = models.IntegerField(verbose_name='Количество')
    archived = models.BooleanField(default=False, verbose_name='Статус')

    @property
    def description_short(self):
        if len(self.description) < 50:
            return self.description
        return self.description[:48] + "..."

    def __str__(self):
        return self.name


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name='Промокод')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    products = models.ManyToManyField(
        Product,
        related_name="orders",
        limit_choices_to={"archived": False},
        verbose_name='Продукты'
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
