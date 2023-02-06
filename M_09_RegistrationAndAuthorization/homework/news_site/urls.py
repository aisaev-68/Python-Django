from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import UserRegisterProfile, NewsList, NewsCreate


app_name = "news_site"
urlpatterns = [
    path("", NewsList.as_view(), name="news_list"),
    path("create/", NewsCreate.as_view(), name="create_news"),

    # path("products/", ProductList.as_view(), name="products_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)