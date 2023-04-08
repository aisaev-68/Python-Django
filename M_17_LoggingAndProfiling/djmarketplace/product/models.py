import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from shopapp.models import Shop


def get_upload_path_by_products(instance, filename):
    return os.path.join('product_images/', now().date().strftime("%Y/%m/%d"), filename)


class Product(models.Model):
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["price"]

    shops = models.ManyToManyField(Shop, related_name="products", through="ShopItem", verbose_name=_("Shops"))
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    attributes = models.JSONField(default=dict, blank=True, verbose_name=_('Attributes'))
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.CASCADE, null=True)
    rating = models.FloatField(verbose_name=_('Rating'), blank=True, default=0.0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Price'))
    image = models.ImageField(upload_to=get_upload_path_by_products, verbose_name=_('Image product'),
                              default='default_images/default_image.jpg')
    discount = models.SmallIntegerField(default=0, verbose_name=_('Discount'))
    new_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('New price'))
    sold = models.PositiveSmallIntegerField(default=0, verbose_name=_('Sold'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
    products_count = models.PositiveSmallIntegerField(default=0, verbose_name=_('Count'))
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
    def get_new_price(self):
        return self.new_price
        # return (self.price - round(self.price * self.discount / 100))

    @property
    def progress(self):
        return int((self.sold / self.products_count) * 100)

    def to_json(self):
        product = {
            "pk": self.pk,
            "shop_name": self.shops,
            "name": self.name,
            "description": self.description,
            "attributes": self.attributes,
            "created_by": self.created_by,
            "rating": self.rating,
            "price": self.price,
            "new_price": self.new_price,
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


class ShopItem(models.Model):
    class Meta:
        verbose_name = _("Shop product")
        verbose_name_plural = _("Shop products")

    shop = models.ForeignKey(Shop, related_name="items", on_delete=models.CASCADE, verbose_name=_("Shops"))
    product = models.ForeignKey(Product, related_name="shop_items", on_delete=models.CASCADE, verbose_name=_("Products"))

    def __str__(self):
        return f"{self.shop} {self.product}"