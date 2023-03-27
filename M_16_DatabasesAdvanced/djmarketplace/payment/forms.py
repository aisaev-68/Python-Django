from django.forms import ModelForm

from payment.models import Billing


class BillingForm(ModelForm):
    class Meta:
        model = Billing
        # fields = ["user", "created_at", "amount"]
        fields = ["amount"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["amount"].widget.attrs['style'] = "width: 5vw;"