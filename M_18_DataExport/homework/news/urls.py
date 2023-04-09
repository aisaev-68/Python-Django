from django.urls import path

from news.views import NewsView

name = "news"
urlpatterns = [
    path('', NewsView.as_view(), name="news-list"),
]