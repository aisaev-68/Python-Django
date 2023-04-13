from django.urls import path

from news.views import NewsView, NewsDetail

name = "news"
urlpatterns = [
    path('', NewsView.as_view(), name="news-list"),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
]