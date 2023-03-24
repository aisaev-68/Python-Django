from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from cart.cart import Cart
from cart.forms import CartAddProductForm
from order.forms import OrderModelForm
from product.models import Product


class CartDetail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderModelForm()
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                         'update': True})

        return render(request, 'shopapp/cart.html', context={'cart': cart, 'form': form})


class CartAdd(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        cart.add(
                product=product,
                quantity=1,
                update_quantity=False,
            )
        return redirect('shopapp:shop_page')


class CartDelete(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse_lazy(
            "shopapp:cart_detail",
        )

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cart.remove(product)
        url = self.get_success_url()
        return HttpResponseRedirect(url)


class CartUpdate(LoginRequiredMixin, View):

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dif_count = product.products_count - cd['quantity']
            if dif_count >= 0:
                cart.add(
                    product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'],
                )
        return redirect('shopapp:cart_detail')

        # return render(request, 'shopapp/cart.html', context={'cart': cart, 'form': form, 'message': f'Only {product.products_count} products left.'})


