from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from payment.forms import BillingForm
from payment.models import Billing


class BillView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            "form_invoice": BillingForm(),
            "billing": Billing.objects.filter(user=request.user).first()
        }
        return render(request, "shopapp/account_top_up.html", context=context)

    def post(self, request, *args, **kwargs):
        form_invoice = BillingForm(request.POST)
        if form_invoice.is_valid():
            user = User.objects.get(pk=request.user.pk)

            cd = form_invoice.cleaned_data["replenishment_amount"]
            if user:
                user_amount = Billing.objects.filter(user=user).filter(balance__gt=0).first()

                if user_amount:

                    Billing.objects.create(
                        replenishment_amount=cd,
                        balance=cd + user_amount.balance,
                        user=request.user,
                    )
                    user_amount.balance = 0
                    user_amount.save()
                else:

                    Billing.objects.create(
                        replenishment_amount=cd,
                        balance=cd,
                        user=request.user,
                    )

        return render(request, "shopapp/shop-list.html")


class HistoryBillView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            "payments": Billing.objects.filter(user=request.user).all()
        }

        return render(request, "shopapp/balance_history.html", context=context)


class InvoiceView(View):
    pass
