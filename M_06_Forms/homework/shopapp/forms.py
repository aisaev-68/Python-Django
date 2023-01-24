from django.forms import ModelForm
from .models import Product


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
