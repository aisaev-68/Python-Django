from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.forms import ModelMultipleChoiceField, SelectMultiple
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

from .models import Product, Order


# def shop(request: HttpRequest):
#     return render(request, 'shopapp/shop.html')
class ShopPage(View):
    def get(self, request: HttpRequest):
        if request.COOKIES.get("sessionid", None):
            return render(request, 'shopapp/shop.html')
        else:
            return render(request, 'shopapp/main.html')


class UserLogIn(LoginView):
    template_name = "shopapp/login.html"
    fields = ["username", "password"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'class': 'username'})
        form.fields['password'].widget.attrs.update({'class': 'password'})
        return form


class UserLogOut(LogoutView):
    next_page = '/'


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


class OrderCreate(CreateView):
    model = Order
    template_name = 'shopapp/create_order.html'
    fields = ["promocode", "delivery_address", "user", "products"]

    success_url = reverse_lazy("shopapp:orders_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['promocode'].widget.attrs.update({'class': 'promocode'}, size='40')
        form.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'}, size='40')
        form.fields['user'].widget.attrs.update({'class': 'user'})
        form.fields["products"] = ModelMultipleChoiceField(
            queryset=Product.objects.all(),
            widget=SelectMultiple(
                attrs={'class': 'chosen', }
            ),
            required=True)
        return form


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
        form.fields['promocode'].widget.attrs.update({'class': 'promocode'}, size='40')
        form.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'}, size='40')
        form.fields['user'].widget.attrs.update({'class': 'user'})
        form.fields['products'].widget.attrs.update({'class': 'products'}, size='5')
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
