from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.translation import gettext_lazy as _
from news.models import News
from django.urls import reverse

class NewsRssFeed(Feed):
    title = _("News")
    link = "latest/feed/"
    description = _("Latest news")

    def items(self):
        return News.objects.filter(published=False).order_by("-created_at")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.description, 10)

    def item_link(self, item):
        return reverse('news_detail', args=[item.pk])
