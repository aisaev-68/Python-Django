from django import forms
from django.forms import ModelForm, ChoiceField
from django.forms.widgets import CheckboxSelectMultiple, SelectMultiple
from .models import Product, Order


class ProductModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'name'}, size='40')
        self.fields['description'].widget.attrs.update({'class': 'description'}, size='40')
        self.fields['price'].widget.attrs.update({'class': 'price'}, min_value=0, size='40')
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs.update({'class': 'discount'}, size='40')
        self.fields['discount'].widget.attrs['min'] = 0

    class Meta:
        model = Product
        fields = ["name", "description", "price", "discount"]


class OrderModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['promocode'].widget.attrs.update({'class': 'promocode'}, size='40')
        self.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'}, size='40')
        self.fields['user'].widget.attrs.update({'class': 'user'})
        # self.fields['products'].widget.update({'class': 'products'})
        self.fields["products"] = ChoiceField(choices=[(product.pk, product.name) for product in Product.objects.all()])
        self.fields['products'].widget.attrs.update({'class': 'products'})
        # self.fields["products"].widget = SelectMultiple(attrs={'class': 'chosen'})
        # self.fields["products"].queryset = Product.objects.all()


    class Meta:
        model = Order
        fields = ["promocode", "delivery_address", "user", "products"]
