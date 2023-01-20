from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from . import models


def index(request: HttpRequest):
    return render(request, 'shopapp/shop.html')


def products(request: HttpRequest):
    product_lst = models.Product.objects.all()
    return render(request, 'shopapp/products.html', {"products": product_lst})


def orders(request: HttpRequest):
    orders = models.Order.objects.all()
    orders_lst = []
    for order in orders:
        order = {
            "promocode": order.promocode,
            "delivery_address": order.delivery_address,
            "created_at": order.created_at,
            "user": order.user,
            "product": [a.name for a in order.product.all()]
        }
        orders_lst.append(order)
    return render(request, 'shopapp/orders.html', {"orders": orders_lst})

