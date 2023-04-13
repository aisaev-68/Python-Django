from django.urls import path

from houseroom.views import SaleListView, Contact, About, HouseDetail

name = "houseroom"
urlpatterns = [
    path('', SaleListView.as_view(), name="sale"),
    path("contact/", Contact.as_view(), name="contact"),
    path("about/", About.as_view(), name="about"),
    path("detail/<int:pk>/", HouseDetail.as_view(), name="house_detail"),
]