from django.forms import HiddenInput, ModelForm
from django.utils.translation import gettext_lazy as _
from order.models import Order


class OrderModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].widget = HiddenInput()
        self.fields['user'].required = False
        self.fields['paid'].widget = HiddenInput()
        self.fields['promocode'].widget.attrs['style'] = "width: 25vw;"
        self.fields['delivery_address'].widget.attrs['style'] = "width: 25vw;"
        self.fields['delivery_address'].required = True
        self.fields['delivery_address'].label = _('Delivery address')
        self.fields['promocode'].label = _('Promocode')
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Order
        fields = ["user", "promocode", "delivery_address", "paid"]