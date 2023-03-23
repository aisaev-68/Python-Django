from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product


class Billing(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.CASCADE, null=True,
                             related_name='billings')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of payment/Invoice added'))
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Replenishment amount'))

    def __str__(self):
        return '{} {}'.format(self.user, self.amount)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Billing")
        verbose_name_plural = _("Billings")


class Invoice(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Created by'), on_delete=models.CASCADE, null=True,
                             related_name='invoices')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of payment for the goods'))
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Payment amount'))
    product = models.ForeignKey(Product, related_name='invoices', on_delete=models.CASCADE,
                                verbose_name=_('Products'))

    def __str__(self):
        return '{} {}'.format(self.user, self.amount)

    def products_list(self):
        return [product.name for product in self.product.all()]

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

