import json

from django.http import HttpRequest, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_datetime
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy
from django.forms import HiddenInput
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

from .cart import Cart
from .models import Product, Order, Category, Catalog, OrderItem
from .forms import OrderModelForm, ProductModelForm, ContactForm, CartAddProductForm, CategoryModelForm


class ShopPage(View):
    def get(self, request: HttpRequest):
        results = Product.objects.filter(archived=False)
        cart = Cart(request)
        context = {
            "products": results,
            "cart": cart,
        }
        return render(request, 'shopapp/first-page.html', context=context)


class ShowProductsPage(View):
    def get(self, request: HttpRequest, slug=None):
        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        print(888888888888, slug)
        category = Category.objects.filter(slug=slug).first()
        print(888888888888, category.catalog)
        results = Product.objects.filter(archived=False, catalog=category.catalog, category=category)
        context = {
            "products": results,
            "categories": Category.objects.filter(catalog=category.catalog.pk),
            "cart": cart,
            "form": form,
        }
        return render(request, 'shopapp/shop-list.html', context=context)


class CatalogProducts(View):
    def get(self, request, eng_name):
        cart = Cart(request)
        print(111111111111111)
        form = CartAddProductForm(request.POST)
        catalog = Catalog.objects.filter(eng_name=eng_name).first()
        category = Category.objects.filter(catalog=catalog)
        results = Product.objects.filter(archived=False, catalog=catalog)
        context = {
            "products": results,
            "categories": category,
            "cart": cart,
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
        context_data['form'] = form = CartAddProductForm(self.request.POST)
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
        print(888, context)
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
        # orders = Order.objects.select_related("user").prefetch_related("products").filter(
        #     user=kwargs['pk']).all()
        orders = Order.objects.filter(user=kwargs['pk']).all()

        if orders:
            for order in orders:
                orders_data = order.items.all()
                for order_product in orders_data:

                    dict_order = {}

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
        print(5, [c for c in cart])
        product = get_object_or_404(Product, pk=product_id)
        print(6666666, self.kwargs)
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

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cart.remove(product)
        url = self.get_success_url()
        return HttpResponseRedirect(url)


class CartUpdate(LoginRequiredMixin, View):

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        print(1, [c for c in cart])
        form = CartAddProductForm(request.POST)
        print(2222, form)
        if form.is_valid():
            print(3333, product)
            cd = form.cleaned_data
            print(4444, cd)
            dif_count = product.products_count - cd['quantity']
            if dif_count >= 0:
                cart.add(
                    product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'],
                )
        return redirect('shopapp:cart_detail')

        # return render(request, 'shopapp/cart.html', context={'cart': cart, 'form': form, 'message': f'Only {product.products_count} products left.'})


class ProductOffer(LoginRequiredMixin, View):
    # template_name = 'shopapp/offers.html'
    def get(self, request):
        return render(request, 'shopapp/offers.html')