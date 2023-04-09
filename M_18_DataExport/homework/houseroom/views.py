from django.shortcuts import render, redirect
from django.views import View

from houseroom.forms import ContactForm
from houseroom.models import HouseRoom


class SaleListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "sale_rooms": HouseRoom.objects.all()
        }
        return render(request, "houseroom/properties_sale-list.html", context=context)


class Contact(View):
    form_class = ContactForm
    template_name = "houseroom/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, "houseroom/about.html")
