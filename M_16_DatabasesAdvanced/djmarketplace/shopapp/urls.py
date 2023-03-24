from django.urls import path, include

from product.views import ShowProductsPage
from shopapp.views import ShopView, Contact

name = "shopapp"
urlpatterns = [
    path("", ShopView.as_view(), name='shops'),
    path('products/', include('product.urls'), name="products"),
    path("contact/", Contact.as_view(), name="contact"),
    path('cart/', include('cart.urls'), name="cart"),
    path('profile/', include('app_users.urls'), name="accounts"),
    path('orders/', include('order.urls'), name="orders"),
]