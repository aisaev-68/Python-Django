from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms import HiddenInput
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView

from cart.cart import Cart
from cart.forms import CartAddProductForm
from product.forms import ProductModelForm
from product.models import Product
from shopapp.models import Shop


class ShowProductsPage(View):
    def get(self, request: HttpRequest, pk=None):

        form = CartAddProductForm(request.POST)
        shop = Shop.objects.filter(pk=pk).first()
        results = Product.objects.filter(archived=False, shop=shop)
        context = {
            "products": results,
            "form": form,
        }
        return render(request, 'shopapp/shop-list.html', context=context)





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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = CartAddProductForm(self.request.POST)
        return context_data


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

