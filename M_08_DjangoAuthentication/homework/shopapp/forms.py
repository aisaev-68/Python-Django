from django.forms import ModelForm, MultipleChoiceField
from django.forms.widgets import SelectMultiple
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
        fields = ["name", "description", "price", "discount", "archived"]


class OrderModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['promocode'].widget.attrs.update({'class': 'promocode'}, size='40')
        self.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'}, size='40')
        self.fields['user'].widget.attrs.update({'class': 'user'})
        self.fields['products'].value = "Продукты"
        self.fields["products"] = MultipleChoiceField(
            choices=[(product.pk, product.name) for product in Product.objects.all()],
            widget=SelectMultiple(
                attrs={'class': 'chosen',}
            ),
            required=False)


    class Meta:
        model = Order
        fields = ["promocode", "delivery_address", "user", "products"]

