from django.urls import path
from django.contrib.auth import views

from shopapp.views import ShopView

# from .views import S
#
name = 'shopapp'
urlpatterns = [
    path('all_shops/', ShopView.as_view(), name='shops'),
]