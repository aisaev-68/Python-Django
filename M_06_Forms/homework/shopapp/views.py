from timeit import default_timer


from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductModelForm, OrderModelForm
from .models import Product, Order


def shop(request: HttpRequest):

    return render(request, 'shopapp/shop.html')


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    # context = {
    #     "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    # }
    context = {
        "orders": Order.objects.all(),
    }
    print(context)
    return render(request, 'shopapp/orders-list.html', context=context)


def create_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("shopapp:products_list"))
    else:
        form = ProductModelForm()
    return render(request, 'shopapp/create-product.html', {'form': form})


def create_order(request: HttpRequest):
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("shopapp:orders_list"))
    else:
        form = OrderModelForm()
    return render(request, 'shopapp/create-order.html', {'form': form})