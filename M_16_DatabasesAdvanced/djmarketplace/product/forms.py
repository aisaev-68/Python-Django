from django.forms import SelectMultiple, ModelChoiceField, ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from product.models import Product
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