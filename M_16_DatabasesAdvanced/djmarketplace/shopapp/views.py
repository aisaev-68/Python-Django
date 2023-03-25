from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms import HiddenInput
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView

from cart.cart import Cart
from cart.forms import CartAddProductForm
from product.models import Product
from .forms import ContactForm
from .models import Shop


class ShopView(View):
    def get(self, request):
        return render(request, 'shopapp/shop-list.html')




class Contact(View):
    form_class = ContactForm
    template_name = "shopapp/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})