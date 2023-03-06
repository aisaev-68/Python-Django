import json

from django.http import HttpRequest, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.dateparse import parse_datetime
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy
from django.forms import HiddenInput
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

from .models import Product, Order, Category
from .forms import OrderModelForm, ProductModelForm, ContactForm


class ShopPage(View):

    def get(self, request: HttpRequest):
        context = {"products": Product.objects.filter(archived=False), "categories": Category.objects.all()}
        return render(request, 'shopapp/main.html', context=context)


class ProductList(ListView):
    # model = Product
    context_object_name = "products"
    template_name = 'shopapp/products-list.html'
    queryset = Product.objects.filter(archived=False)


class DetailProduct(DetailView):
    form_class = ProductModelForm
    context_object_name = "products"
    template_name = 'shopapp/product_detail.html'

    def get_queryset(self):
        queryset = Product.objects.filter(pk=self.kwargs['pk'])
        return queryset


class ArchivedProduct(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = "products"
    template_name = 'shopapp/product_archived.html'

    def get_success_url(self):
        return reverse_lazy(
            "shopapp:products_list",
        )

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super().post(request, *args, **kwargs)


class CreateProduct(LoginRequiredMixin, CreateView):
    # model = Product
    form_class = ProductModelForm
    template_name = 'shopapp/create_product.html'
    success_url = reverse_lazy("shopapp:products_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['created_by'].widget = HiddenInput()
        return form

    def get_initial(self):
        self.initial['created_by'] = self.request.user.id
        return self.initial


class UpdateProduct(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm
    template_name = 'shopapp/update_product.html'

    def get_success_url(self):
        return reverse(
            "shopapp:product_detail",
            kwargs={"pk": self.object.pk},
        )

    def get_queryset(self):
        queryset = Product.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def test_func(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        # self.request.user.groups.filter(name='Edit').exists()
        return self.request.user.is_superuser or self.request.user == product.created_by


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = "orders"
    template_name = 'shopapp/orders-list.html'


class OrderCreate(LoginRequiredMixin, CreateView):
    form_class = OrderModelForm
    template_name = 'shopapp/create_order.html'

    def get_success_url(self):
        return reverse(
            "shopapp:orders_user",
            kwargs={"pk": self.request.user.pk},
        )

    def get_initial(self):
        return {'user': self.request.user}


class OrderListByUser(LoginRequiredMixin, ListView):
    model = OrderModelForm
    context_object_name = "orders"
    template_name = 'shopapp/orders-list.html'

    def get_queryset(self):
        queryset = Order.objects.select_related("user").prefetch_related("products").filter(
            user=self.kwargs['pk']).all()

        return queryset


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
    queryset = Order.objects.select_related("user").prefetch_related("products").all()


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


class Contact(View):
    form_class = ContactForm
    template_name = "shopapp/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})


class OrdersExport(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        orders = Order.objects.select_related("user").prefetch_related("products").all()
        list_orders = []
        for order in orders:
            data = {
                "id": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "created_at": parse_datetime(str(order.created_at)).strftime('%Y-%m-%d %H:%M:%S'),
                "user": order.user.pk,
                "products": [p.pk for p in order.products.all()]
            }
            list_orders.append(data)
        return HttpResponse(json.dumps({'all-orders': list_orders}), content_type="application/json")

    def test_func(self):
        return self.request.user.is_staff
