from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import NewsList, NewsCreate


app_name = "news_site"
urlpatterns = [
    path("", NewsList.as_view(), name="news_list"),
    path("create/", NewsCreate.as_view(), name="create_news"),
]