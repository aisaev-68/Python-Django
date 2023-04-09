from django.urls import path

from houseroom.views import SaleListView, Contact, About

name = "houseroom"
urlpatterns = [
    path('', SaleListView.as_view(), name="sale"),
    path("contact/", Contact.as_view(), name="contact"),
    path("about/", About.as_view(), name="about"),
]