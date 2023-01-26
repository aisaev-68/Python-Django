from timeit import default_timer


from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.forms import ChoiceField, BooleanField
from django.urls import reverse, reverse_lazy
# from .forms1 import ProductModelForm, OrderModelForm
from .models import Product, Order


def shop(request: HttpRequest):

    return render(request, 'shopapp/shop.html')


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
    # fields = ["archived",]
    # success_url = reverse_lazy("shopapp:products_list")

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['name'].widget.attrs.update({'class': 'name'}, size='40')
    #     form.fields['description'].widget.attrs.update({'class': 'description'}, size='40')
    #     form.fields['price'].widget.attrs.update({'class': 'price'}, min_value=0, size='40')
    #     form.fields['price'].widget.attrs['min'] = 0
    #     form.fields['discount'].widget.attrs.update({'class': 'discount'}, size='40')
    #     form.fields['discount'].widget.attrs['min'] = 0
    #     return form

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
    fields = ["name", "description", "price", "discount",]

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

        # form.fields["archived"] = ChoiceField(choices=[(1, True), (2, False)])
        # form.fields['archived'].widget.attrs["archived"] = "Статус"
        # form.fields['archived'].widget.attrs.update({'class': 'archived'})
        return form


class OrderList(ListView):
    model = Order
    context_object_name = "orders"
    template_name = 'shopapp/orders-list.html'
    # queryset = Order.objects.select_related("user").prefetch_related("products").all()


class OrderCreate(CreateView):
    model = Order
    template_name = 'shopapp/create_order.html'
    fields = ["promocode", "delivery_address", "user", "products"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['promocode'].widget.attrs.update({'class': 'promocode'}, size='40')
        form.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'}, size='40')
        form.fields['user'].widget.attrs.update({'class': 'user'})
        form.fields["products"] = ChoiceField(choices=[(product.pk, product.name) for product in Product.objects.all()])
        form.fields['products'].widget.attrs.update({'class': 'products'})
        return form


class UpdateOrder(UpdateView):
    model = Order
    template_name = 'shopapp/update_order.html'
    fields = ["name", "description", "price", "discount"]