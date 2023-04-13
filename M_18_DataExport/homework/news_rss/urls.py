from django.urls import path

from news_rss.feeds import NewsRssFeed

name = "news_rss"
urlpatterns = [
    path('latest/feed/', NewsRssFeed(), name="news_rss"),
]