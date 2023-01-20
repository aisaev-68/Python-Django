from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from . import models


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'shopapp/shop.html')


def products(request: HttpRequest) -> HttpResponse:
    product_lst = models.Product.objects.all()
    return render(request, 'shopapp/products.html', {"products": product_lst})


def orders(request: HttpRequest) -> HttpResponse:
    orders = models.Order.objects.select_related("user").prefetch_related("product").all()
    return render(request, 'shopapp/orders.html', {"orders": orders})
