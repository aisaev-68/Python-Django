from django.urls import path
from .views import shop_index, products_list

app_name = 'shopapp'
urlpatterns = [
    path('shop/', shop_index, name='index'),
    path('product/', products_list, name='product'),
]