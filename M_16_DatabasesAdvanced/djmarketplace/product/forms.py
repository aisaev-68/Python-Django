from django.forms import ModelChoiceField, ModelForm, ImageField, FileInput, CharField, \
    CheckboxSelectMultiple, ModelMultipleChoiceField, Form, SelectMultiple, HiddenInput, MultipleChoiceField, Textarea
from django.utils.translation import gettext_lazy as _
from product.models import Product
from shopapp.models import Shop


class ShopModelForm(ModelForm):

    shop_name = ModelMultipleChoiceField(
        queryset=Shop.objects.all(),
        widget=CheckboxSelectMultiple,
    )

    class Meta:
        model = Shop
        fields = ["shop_name"]




class ProductModelForm(ModelForm):
    image = ImageField(
        label=_("Image product"),
        required=False,
        widget=FileInput()
    )
    shop_name = MultipleChoiceField(
        choices=tuple([(shop.pk, shop.shop_name) for shop in Shop.objects.all()]),
        widget=CheckboxSelectMultiple,
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['price'].widget.attrs['max'] = 10000000
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 5
        self.fields['discount'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs['max'] = 30
        self.fields['products_count'].widget.attrs['min'] = 0
        self.fields['sold'].widget.attrs['min'] = 0
        self.fields['created_by'].widget = HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Product
        fields = ["shop_name", "name", "brand", "description", "attributes", "rating", "price", "created_by", "discount", "image",
                  "products_count", "sold"]
