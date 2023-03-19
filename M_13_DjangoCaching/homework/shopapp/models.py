import os
from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.urls import resolve
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


def get_upload_path_by_products(instance, filename):
    return os.path.join('product_images/', now().date().strftime("%Y/%m/%d"), filename)


class Shop(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Name'))
    address = models.CharField(max_length=200, db_index=True, verbose_name=_('Address'))


class Catalog(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Name'))
    eng_name = models.CharField(max_length=100, db_index=True, verbose_name=_('English name'))

    # slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-name', ]
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shopapp:catalog_products", kwargs={'eng_name': self.eng_name})

    def to_json(self):
        return {
            self.name: [category for category in self.categories.all()]
        }


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Name'))
    slug = models.SlugField(max_length=200, db_index=True)
    catalog = models.ForeignKey(Catalog, related_name='categories', on_delete=models.CASCADE,
                                verbose_name=_('Catalog'))


    class Meta:
        ordering = ['name', ]
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shopapp:products_by_category", kwargs={'slug': self.slug})

    def get_products_by_category(self):
        return {
            self.name: [product.to_json() for product in self.products]
        }

class Product(models.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name", "price"]

    catalog = models.ForeignKey(Catalog, related_name='products', on_delete=models.CASCADE,
                                 verbose_name=_('Catalog'))
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                verbose_name=_('Category'))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    attributes = models.JSONField(default=dict, blank=True, verbose_name=_('Attributes'))
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.CASCADE, null=True)
    rating = models.FloatField(verbose_name=_('Rating'), blank=True, default=0.0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(upload_to=get_upload_path_by_products, verbose_name=_('Image product'),
                              default='images/default_image.jpg')
    discount = models.SmallIntegerField(default=0, verbose_name=_('Discount'))
    sold = models.SmallIntegerField(default=0, verbose_name=_('Sold'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
    products_count = models.IntegerField(verbose_name=_('Count'))
    archived = models.BooleanField(default=False, verbose_name=_('Status'))
    brand = models.CharField(max_length=100, verbose_name=_('Brand'))

    @property
    def description_short(self):
        if len(self.description) < 50:
            return self.description
        return self.description[:48] + "..."

    def __str__(self):
        return f"{self.name}"

    @property
    def get_old_price(self):
        return (self.price - round(self.price * self.discount / 100))

    @property
    def progress(self):
        return int((self.sold / self.products_count) * 100)

    def to_json(self):
        product = {
            "pk": self.pk,
            "catalog": self.catalog.name,
            "catalog_eng": self.catalog.eng_name,
            "name": self.name,
            "description": self.description,
            "attributes": self.attributes,
            "created_by": self.created_by,
            "rating": self.rating,
            "price": self.price,
            "old_price": self.get_old_price,
            "image": self.image,
            "discount": self.discount,
            "sold": self.sold,
            "created_at": self.created_at,
            "products_count": self.products_count,
            "archived": self.archived,
            "progress": self.progress,
            "dif_count_products": (self.products_count - self.sold),
            "brand": self.brand,
        }
        return product

    @classmethod
    def get_products_by_category(cls, pk):
        return cls.objects.filter(archived=False, category=pk)


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True, verbose_name=_('Delivery address'))
    promocode = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Promo code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create order date'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('User'))
    paid = models.BooleanField(default=False, verbose_name=_('Status'))


    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return "Order {}".format(self.delivery_address)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name=_('Orders'))
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name=_('Products'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))


    def get_price(self):
        return Product.objects.filter(name=self.product).first().price

    def __str__(self):
        return '{}'.format(self.price)

    def get_sum(self):
        return self.price * self.quantity