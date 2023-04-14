from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import HouseRoom
from news.models import News

class NewsSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return News.objects.all()

    def lastmod(self, item):
        return item.created_at

    # def location(self, item):
    #     return reverse(item, args=[item.pk])

class HouseRoomSitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return HouseRoom.objects.all()

    def lastmod(self, item):
        return item.created_at

    # def location(self, item):
    #     return reverse(item, args=[item.pk])

# class AboutSitemap(Sitemap):
#
#     changefreq = 'weekly'
#     priority = 0.9
#     def items(self):
#         return ['about']
#
#     def lastmod(self, item):
#         return item