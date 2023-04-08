from django.shortcuts import render
from django.views import View
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