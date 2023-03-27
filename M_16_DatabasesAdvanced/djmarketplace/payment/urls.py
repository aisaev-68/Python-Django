from django.urls import path
from django.contrib.auth import views

from .views import BillView, InvoiceView

app_name = "payment"
urlpatterns = [
    path("", BillView.as_view(), name="account_top_up"),
    path("invoice/", InvoiceView.as_view(), name="invoice"),
]