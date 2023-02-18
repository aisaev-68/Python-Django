import os

from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, ModelForm, MultipleChoiceField, ModelMultipleChoiceField
from django.forms.widgets import SelectMultiple, HiddenInput, CheckboxSelectMultiple, ClearableFileInput
from .models import Product, Order


class ProductModelForm(ModelForm):
    image = forms.ImageField(
        label="Изображение продукта",
        required=False,
        widget=forms.FileInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['price'].widget.attrs['min'] = 10000000
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 5
        self.fields['discount'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs['max'] = 30
        self.fields['products_count'].widget.attrs['min'] = 0
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Product
        fields = ["name", "description", "attributes", "rating", "price", "created_by", "discount", "image",
                  "products_count"]


class OrderModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["products"] = ModelMultipleChoiceField(
            queryset=Product.objects.all(),
            label='Продукты',
            widget=SelectMultiple(attrs={
                "class": "form-select",
            }, ),
        )
        self.fields['user'].widget = HiddenInput()
        self.fields['products'].widget.attrs.update(rows=4)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Order
        fields = ["user", "promocode", "delivery_address", "products"]


class ContactForm(forms.Form):
    first_name = forms.CharField(label="Имя", )
    last_name = forms.CharField(label="Фамилия", )
    email = forms.EmailField(label="Email", )
    message = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'rows': 3}))
