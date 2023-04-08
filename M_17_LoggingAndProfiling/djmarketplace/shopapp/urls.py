from django.urls import path, include

from product.views import ShowProductsPage
from shopapp.views import ShopView, Contact

name = "shopapp"
urlpatterns = [
    path("", ShopView.as_view(), name='shops'),
]