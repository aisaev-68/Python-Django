from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import models

def index(request: HttpRequest):
    return render(request, 'shopapp/shop.html')


def products(request: HttpRequest):
    product_lst = models.Product.objects.all()
    return render(request, 'shopapp/products.html', {"products": product_lst})