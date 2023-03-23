from django.urls import path
from django.contrib.auth import views

from .views import BillingView, InvoiceView

app_name = "payment"
urlpatterns = [
    path("billing/", BillingView.as_view(), name="billing"),
    path("invoice/", InvoiceView.as_view(), name="invoice"),
]