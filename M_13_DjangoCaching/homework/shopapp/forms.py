from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import SelectMultiple, HiddenInput
from .models import Product, Order, Category


class CatalogModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''


class CategoryModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''


class ProductModelForm(ModelForm):
    image = forms.ImageField(
        label=_("Image product"),
        required=False,
        widget=forms.FileInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"] = ModelChoiceField(
            queryset=Category.objects.all(),
            label=_('Categories'),
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
        fields = ["name", "brand", "category", "description", "attributes", "rating", "price", "created_by", "discount", "image",
                  "products_count", "sold"]


class OrderModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].widget = HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Order
        fields = ["user", "promocode", "delivery_address", "paid"]


class ContactForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), )
    last_name = forms.CharField(label=_("Last name"), )
    email = forms.EmailField(label="Email", )
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'rows': 3, 'cols': 20,}))


class CartAddProductForm(forms.Form):
    # PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    quantity = forms.IntegerField(
        label=_('Quantity'),
    )
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput
                                )

