from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from payment.forms import BillingForm
from payment.models import Billing


class BillView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "form_invoice": BillingForm()
        }
        return render(request, "shopapp/account_top_up.html", context=context)

    def post(self, request, *args, **kwargs):
        form_invoice = BillingForm(request.POST)
        if form_invoice.is_valid():
            user = User.objects.get(pk=request.user.pk)

            cd = form_invoice.cleaned_data["amount"]
            if user:
                user_amount = Billing.objects.filter(user=user).filter(amount__gt=0).first()

                if user_amount:
                    print(9999, user_amount.amount)
                    Billing.objects.create(
                        amount=cd + user_amount.amount,
                        user=request.user,
                    )
                    user_amount.amount = 0
                    user_amount.save()
                else:
                    Billing.objects.create(
                        amount=cd,
                        user=request.user,
                    )

        return redirect("shops")


class InvoiceView(View):
    pass
