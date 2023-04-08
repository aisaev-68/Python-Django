from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True, verbose_name=_('Delivery address'))
    promocode = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Promo code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Create order date'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('User'), related_name="orders")
    paid = models.BooleanField(default=False, verbose_name=_('Status'))

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return "Order {}".format(self.delivery_address)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name=_('Orders'))
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE,
                                verbose_name=_('Products'))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Total price'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))

    def get_price(self):
        return Product.objects.filter(name=self.product).first().price

    def __str__(self):
        return '{}'.format(self.total_price)


