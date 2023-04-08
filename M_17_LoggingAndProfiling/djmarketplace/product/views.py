import datetime

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Sum
from django.forms import HiddenInput
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.cart import Cart
from cart.forms import CartAddProductForm
from order.models import OrderItem
from product.forms import ProductModelForm, ShopModelForm
from product.models import Product, ShopItem
from shopapp.models import Shop


class ShowProductsPage(View):
    def get(self, request: HttpRequest, pk=None):

        form = CartAddProductForm()
        products = Product.objects.prefetch_related('shops').filter(shops=pk).filter(archived=False)
        results = products.all()
        # prod_count = products.count()
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        paginator = Paginator(results, 8)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
        context = {
            "form": form,
            "page": results,
            # "prod_count": prod_count,
        }
        return render(request, 'shopapp/shop-list.html', context=context)


class ProductList(ListView):
    # model = Product
    context_object_name = "products"
    template_name = 'shopapp/products-list.html'
    paginate_by = 8
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


class CreateProduct(LoginRequiredMixin, View):

    success_url = reverse_lazy("products_list")

    def get(self, request, *args, **kwargs):
        form = ProductModelForm()
        context = {"form": form}
        return render(request, "shopapp/create_product.html", context=context)


    def post(self, request, *args, **kwargs):
        form = ProductModelForm(request.POST)
        shops = request.POST.getlist("shop_name")
        if form.is_valid():

            cd = form.cleaned_data
            product = Product.objects.create(
                name=cd["name"],
                brand=cd["brand"],
                description=cd["description"],
                attributes=cd["attributes"],
                rating=cd["rating"],
                created_by=request.user.id,
                price=cd["price"],
                new_price=cd["price"] - cd["price"] * cd["discount"] / 100,
                discount=cd["discount"],
                image=cd["image"],
                products_count=cd["products_count"],
                sold=cd["solid"],
                archived=False,
            )
            for shop in shops:
                ShopItem.objects.create(
                    shop_id=shop,
                    product_id=product.pk
                )

            return redirect(self.success_url)


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
        return self.request.user.is_superuser or self.request.user == product.created_by


class TopSellingReport(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        products = Product.objects.filter(
            order_items__order__created_at__lte=datetime.datetime.today(), order_items__order__created_at__gt=datetime.datetime.today() - datetime.timedelta(days=7)
        ).annotate(total=Sum('order_items__quantity')).order_by(
            '-total')[:10]
        context = {
            "products": products
        }
        return render(request, "shopapp/top_selling_report.html", context=context)