from django.urls import path
from . import views

app_name = 'shopapp'
urlpatterns = [
    path('shop/', views.index, name='index'),
    path('product/', views.products, name='products'),
    path('order/', views.orders, name='orders'),
]