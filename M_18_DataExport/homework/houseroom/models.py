import os

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class HouseRoom(models.Model):
    city = models.CharField(max_length=100, verbose_name=_('City'))
    address = models.CharField(max_length=200, verbose_name=_('Address'), blank=True)
    developer = models.CharField(max_length=100, verbose_name=_('Developer'))
    floors = models.IntegerField(verbose_name=_("Floors"))

    class Meta:
        verbose_name = _("House room")
        verbose_name_plural = _("House rooms")
        ordering = ["city",]

    def __str__(self):
        return "HouseRoom {c}, {a}".format(c=self.city, a=self.address)


class RoomType(models.Model):
    type_name = models.CharField(max_length=100, verbose_name=_('Type room'))

    class Meta:
        verbose_name = _("Type room")
        verbose_name_plural = _("Type rooms")
        ordering = ["type_name"]

    def __str__(self):
        return "RoomType {t}".format(t=self.type_name)


class NumberRoom(models.Model):
    house = models.ForeignKey("HouseRoom", related_name="rooms", on_delete=models.CASCADE, verbose_name=_("House room"))
    room_count = models.IntegerField(verbose_name=_("Number of rooms"))
    storey = models.IntegerField(verbose_name=_("Storey"))
    total_area = models.FloatField(verbose_name=_('Total area'), blank=True)
    kitchen_area = models.FloatField(verbose_name=_('Kitchen area'), blank=True)
    living_space = models.FloatField(verbose_name=_('Living space'), blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Price'))
    room_type = models.ForeignKey("RoomType", on_delete=models.CASCADE, related_name="rooms")

    class Meta:
        verbose_name = _("Number of rooms")
        verbose_name_plural = _("Number of rooms")
        ordering = ["room_count"]

    def __str__(self):
        return "NumberRoom {c}".format(c=self.room_count)



