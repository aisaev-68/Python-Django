from django.urls import path
from api.views import NewsListAPIView, HouseRoomAPIView


app_name = "api"
urlpatterns = [
    path('news/', NewsListAPIView.as_view(), name='api_news'),
    path('house/list/', HouseRoomAPIView.as_view(), name='api_house_list'),
]