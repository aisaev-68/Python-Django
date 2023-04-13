from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import HouseRoom


class HouseRoomSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return HouseRoom.object.all()
    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return reverse('house_detail', args=[obj.pk])