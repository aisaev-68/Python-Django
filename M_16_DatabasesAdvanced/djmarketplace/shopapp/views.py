from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView

from product.models import Product
from shopapp.models import Shop




class ShopView(LoginRequiredMixin, View):
    def get(self, request):
        shops = Shop.objects.all()
        return render(request, 'shopapp/all_shops.html', context={"shops": shops})