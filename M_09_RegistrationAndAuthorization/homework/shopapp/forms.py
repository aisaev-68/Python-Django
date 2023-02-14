from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm, MultipleChoiceField, ModelMultipleChoiceField
from django.forms.widgets import SelectMultiple, HiddenInput, CheckboxSelectMultiple
from .models import Product, Order


class ProductModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs['min'] = 0
        self.fields['products_count'].widget.attrs['min'] = 0
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Product
        fields = ["name", "description", "attributes", "rating", "price", "discount", "products_count", "archived"]


class OrderModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['delivery_address'].widget.attrs.update(cols=0, rows=0)
        # self.fields["products"] = MultipleChoiceField(
        #     choices=[(product.pk, product.name) for product in Product.objects.all()],
        #     widget=SelectMultiple(),
        #     required=False)
        self.fields["products"] = ModelMultipleChoiceField(
            queryset=Product.objects.all(),
            label='Продукты',
            widget=SelectMultiple(attrs={
                        "class": "form-select",
                    },),
        )
        self.fields['user'].widget = HiddenInput()
        self.fields['products'].widget.attrs.update(rows=4)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Order
        fields = ["user", "promocode", "delivery_address", "products"]
