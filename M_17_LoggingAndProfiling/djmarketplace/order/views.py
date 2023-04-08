import json
import logging

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import HiddenInput
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.dateparse import parse_datetime
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.views.generic import DeleteView, DetailView, UpdateView

from app_users.models import Profile
from cart.cart import Cart
from order.forms import OrderModelForm
from order.models import Order, OrderItem
from payment.models import Billing
from product.models import Product


logger = logging.getLogger(__name__)


class OrderList(LoginRequiredMixin, View):
    context_object_name = "orders"

    def get(self, request: HttpRequest):
        dict_order = {}
        context = []
        orders = Order.objects.all()
        for order in orders:
            for product in order.products.all():
                count = 0
                for product1 in order.products.all():
                    if product == product1:
                        if dict_order.get(product):
                            count += 1
                        else:
                            count = 1
                dict_order = {
                    "image": product.image,
                    "name": product.name,
                    "price": product.price,
                    "count": count,
                    "sum": count * product.price,
                    'created_at': order.created_at,
                }
            context.append(dict_order)

        return render(request, 'shopapp/orders-list.html', context=context)


class OrderCreate(LoginRequiredMixin, View):

    def get_success_url(self):
        return reverse(
            "orders_user",
            kwargs={"pk": self.request.user.pk},
        )

    def get_initial(self):
        return {'user': self.request.user}

    def post(self, request):
        carts = Cart(request)
        form = OrderModelForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get('delivery_address')
            promocode = form.cleaned_data.get('promocode')
            payment = Billing.objects.filter(user=request.user).filter(balance__gt=0).first()

            if not payment:
                logger.info(_("Your account is empty"))
                return render(request, "shopapp/nomoney.html")

            if (payment.balance - carts.get_total_price()) < 0:
                logger.info(_("There are not enough funds on the account to purchase"))
                return render(request, "shopapp/nomoney.html")

            for cart in carts:
                prod = Product.objects.filter(name=cart["product"]).first()
                if (prod.products_count - cart['quantity']) < 0:
                    logger.info(_("Not enough products in stock to buy"))
                    return render(request, "shopapp/noproduct.html")

                order = Order.objects.create(
                    delivery_address=address,
                    promocode=promocode,
                    user=request.user,
                    paid=True,
                )
                OrderItem.objects.create(
                    order=order,
                    product=cart['product'],
                    total_price=cart['new_price'] * cart['quantity'],
                    quantity=cart['quantity'],
                )
                product = Product.objects.filter(name=cart['product']).first()

                # product.products_count -= cart['quantity']
                product.sold += cart['quantity']
                product.save()

                sum_deb = cart['new_price'] * cart['quantity']
                payment.balance -= sum_deb
                logger.info(_(f'Debited from account: {sum_deb}'))

                payment.save()
                queryset = OrderItem.objects.filter(order__user=request.user).aggregate(Sum("total_price"))
                total = queryset["total_price__sum"]
                logger.info(_('Order created'))

                if 5000 < total < 15000:
                    Profile.objects.filter(user=request.user).update(status="Junior")
                    logger.info(_("User moved to status Junior"))
                elif 15000 <= total < 50000:
                    Profile.objects.filter(user=request.user).update(status="Middle")
                    logger.info(_("User moved to status Middle"))
                elif total >= 50000:
                    Profile.objects.filter(user=request.user).update(status="VIP")
                    logger.info(_("User moved to status VIP"))

            carts.clear()
            url = self.get_success_url()
            return HttpResponseRedirect(url)


class OrderListByUser(LoginRequiredMixin, View):

    def get(self, request: HttpRequest, *args, **kwargs):
        context = []
        orders = Order.objects.filter(user=kwargs['pk']).all()

        if orders:
            for order in orders:
                orders_data = order.items.all()
                for order_product in orders_data:
                    dict_order = {
                        'image': order_product.product.image,
                        'name': order_product.product.name,
                        'price': order_product.product.new_price,
                        'count': order_product.quantity,
                        'sum': order_product.total_price,
                        'created_at': order.created_at,
                        'delivery_address': order.delivery_address,
                    }

                    context.append(dict_order)

        return render(request, 'shopapp/orders-list.html', context={"orders": context})


class UpdateOrder(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'shopapp/update_order.html'
    fields = ["promocode", "delivery_address", "user", "products"]

    def get_success_url(self):
        return reverse(
            "order_detail",
            kwargs={"pk": self.object.pk},
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user'].widget = HiddenInput()
        return form


class OrderDetail(LoginRequiredMixin, DetailView):
    # model = Order
    context_object_name = "orders"
    template_name = 'shopapp/order_detail.html'
    queryset = Order.objects.select_related("user").prefetch_related("items").all()


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    context_object_name = "orders"
    template_name = 'shopapp/delete_order.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy(
            "orders_list",
        )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super().post(request, *args, **kwargs)


class OrdersExport(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        orders = Order.objects.select_related("user").prefetch_related("items").all()
        list_orders = []
        for order in orders:
            data = {
                "id": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "created_at": parse_datetime(str(order.created_at)).strftime('%Y-%m-%d %H:%M:%S'),
                "user": order.user.pk,
                "paid": order.paid,
                "products": [{'name': p.product.name,
                              'price': p.price,
                              'quantity': p.quantity,
                              'sum': p.get_sum()}
                             for p in order.items.all()]
            }
            list_orders.append(data)
        return HttpResponse(json.dumps({'all-orders': list_orders}), content_type="application/json")

    def test_func(self):
        return self.request.user.is_staff
