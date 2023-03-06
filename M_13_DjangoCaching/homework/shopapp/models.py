from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Category'))
    # slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name',]
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


    def __str__(self):
        return self.name



class Product(models.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name", "price"]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name=_('Category'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    attributes = models.JSONField(default=dict, blank=True, verbose_name=_('Attributes'))
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.CASCADE, null=True)
    rating = models.FloatField(verbose_name=_('Rating'), blank=True, default=0.0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(upload_to='images/', verbose_name=_('Image product'),
                              default='images/default_image.jpg')
    discount = models.SmallIntegerField(default=0, verbose_name=_('Discount'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
    products_count = models.IntegerField(verbose_name=_('Count'))
    archived = models.BooleanField(default=False, verbose_name=_('Status'))

    @property
    def description_short(self):
        if len(self.description) < 50:
            return self.description
        return self.description[:48] + "..."

    def __str__(self):
        return self.name


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True, verbose_name=_('Delivery address'))
    promocode = models.CharField(max_length=20, null=False, blank=True, verbose_name=_('Promo code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create order date'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('User'))
    products = models.ManyToManyField(
        Product,
        related_name="orders",
        limit_choices_to={"archived": False},
        verbose_name=_('Products')
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return "Order {}".format(self.delivery_address)
