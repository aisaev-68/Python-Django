from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.forms import ModelMultipleChoiceField, SelectMultiple
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate
from django.forms import Form, HiddenInput
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

from .models import Product, Order
from .forms import OrderModelForm
from .task import main


class ShopPage(View):


    def get(self, request: HttpRequest):
        if request.COOKIES.get("sessionid", None):
            # if Product.objects.all() is None:
            main()
            return render(request, 'shopapp/shop.html')
        else:
            # if Product.objects.all() is None:
            main()
            context = {"products": Product.objects.filter()}
            print(1111, context)
            return render(request, 'shopapp/main.html', context=context)


class ProductList(ListView):
    # model = Product
    context_object_name = "products"
    template_name = 'shopapp/products-list.html'
    queryset = Product.objects.filter(archived=False)


class DetailProduct(DetailView):
    model = Product
    context_object_name = "products"
    template_name = 'shopapp/product_detail.html'


class ArchivedProduct(DeleteView):
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


class CreateProduct(CreateView):
    model = Product
    template_name = 'shopapp/create_product.html'
    fields = ["name", "description", "price", "discount"]
    success_url = reverse_lazy("shopapp:products_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'name'}, size='40')
        form.fields['description'].widget.attrs.update({'class': 'description'}, size='40')
        form.fields['price'].widget.attrs.update({'class': 'price'}, min_value=0, size='40')
        form.fields['price'].widget.attrs['min'] = 0
        form.fields['discount'].widget.attrs.update({'class': 'discount'}, size='40')
        form.fields['discount'].widget.attrs['min'] = 0
        return form


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'shopapp/update_product.html'
    fields = ["name", "description", "price", "discount", ]

    def get_success_url(self):
        return reverse(
            "shopapp:product_detail",
            kwargs={"pk": self.object.pk},
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs.update({'class': 'name'}, size='40')
        form.fields['description'].widget.attrs.update({'class': 'description'}, size='40')
        form.fields['price'].widget.attrs.update({'class': 'price'}, min_value=0, size='40')
        form.fields['price'].widget.attrs['min'] = 0
        form.fields['discount'].widget.attrs.update({'class': 'discount'}, size='40')
        form.fields['discount'].widget.attrs['min'] = 0
        return form


class OrderList(ListView):
    model = Order
    context_object_name = "orders"
    template_name = 'shopapp/orders-list.html'
    # fields = ["pk", "promocode", "delivery_address", "user", "products"]


class OrderCreate(CreateView):
    form_class = OrderModelForm
    template_name = 'shopapp/create_order.html'
    # success_url = reverse_lazy("shopapp:orders_list")

    def get_success_url(self):
        return reverse(
            "shopapp:orders_user",
            kwargs={"pk": self.request.user.pk},
        )
    def get_initial(self):
        return {'user': self.request.user}

class OrderListByUser(ListView):
    model = OrderModelForm
    context_object_name = "orders"
    template_name = 'shopapp/orders-list.html'

    # queryset = Product.objects.filter(archived=False)

    def get_queryset(self):
        queryset = Order.objects.select_related("user").prefetch_related("products").filter(user=self.kwargs['pk']).all()
        print(1111, queryset)
        return queryset


    # def get_success_url(self):
    #     return reverse(
    #         "shopapp:orders_user",
    #         kwargs={"pk": self.request.user.pk},
    #     )


class UpdateOrder(UpdateView):
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
        # form.fields['promocode'].widget.attrs.update({'class': 'promocode'})
        # form.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'})
        # form.fields['user'].widget.attrs.update({'class': 'user'})
        form.fields['user'].widget = HiddenInput()
        # form.fields['products'].widget.attrs.update({'class': 'products'}, size='5')
        return form


class OrderDetail(DetailView):
    # model = Order
    context_object_name = "orders"
    template_name = 'shopapp/order_detail.html'
    queryset = Order.objects.select_related("user").prefetch_related("products").all()


class OrderDelete(DeleteView):
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
