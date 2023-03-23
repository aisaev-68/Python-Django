from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import HiddenInput
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DeleteView, DetailView, UpdateView

from order.models import Order, OrderItem
from product.models import Product


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
            "shopapp:orders_user",
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
            for cart in carts:
                order = Order.objects.create(
                    delivery_address=address,
                    promocode=promocode,
                    user=request.user,
                    paid=True,
                )
                OrderItem.objects.create(
                    order=order,
                    product=cart['product'],
                    price=cart['price'],
                    quantity=cart['quantity'],
                )
                product = Product.objects.filter(name=cart['product']).first()
                product.products_count = product.products_count - cart['quantity']
                product.save()

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
                        'price': order_product.price,
                        'count': order_product.quantity,
                        'sum': order_product.get_sum,
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
            "shopapp:order_detail",
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
            "shopapp:orders_list",
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

