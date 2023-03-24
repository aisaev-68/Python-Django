from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import SelectMultiple, HiddenInput
from product.models import Product
from order.models import Order
from shopapp.models import Shop


class ProductModelForm(ModelForm):
    image = forms.ImageField(
        label=_("Image product"),
        required=False,
        widget=forms.FileInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["shop"] = ModelChoiceField(
            queryset=Shop.objects.all(),
            label=_('Shop'),
            widget=SelectMultiple(attrs={
                "class": "form-select",
            }, ),
        )
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['price'].widget.attrs['max'] = 10000000
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 5
        self.fields['discount'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs['max'] = 30
        self.fields['products_count'].widget.attrs['min'] = 0
        self.fields['sold'].widget.attrs['min'] = 0
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Product
        fields = ["name", "brand", "shop", "description", "attributes", "rating", "price", "created_by", "discount", "image",
                  "products_count", "sold"]





class ContactForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), )
    last_name = forms.CharField(label=_("Last name"), )
    email = forms.EmailField(label="Email", )
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'rows': 3, 'cols': 20,}))


