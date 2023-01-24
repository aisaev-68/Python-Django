from django.forms import ModelForm
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
        self.fields['delivery_address'].widget.attrs.update({'class': 'delivery_address'}, size='40')
        self.fields['promocode'].widget.attrs.update({'class': 'promocode'}, size='40')
        # self.fields['created_at'].widget.attrs.update({'class': 'created_at'}, size='40')
        # self.fields['user'].widget.attrs.update({'class': 'user'}, size='40')
        # self.fields['product'].widget.update({'class': 'product'}, size='40')

    class Meta:
        model = Order
        fields = ["delivery_address", "promocode",]
        # "created_at", "user", "products"]
