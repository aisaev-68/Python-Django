from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import SelectMultiple, HiddenInput
from .models import Product, Order, Category, Catalog


class CatalogModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''


class CategoryModelForm(ModelForm):
    name = forms.CharField(widget=forms.CheckboxInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Category
        fields = ["name", ]

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
            label=_('Category'),
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
        self.fields['user'].required = False
        self.fields['paid'].widget = HiddenInput()
        self.fields['promocode'].widget.attrs['style'] = "width: 25vw;"
        self.fields['delivery_address'].widget.attrs['style'] = "width: 25vw;"
        self.fields['delivery_address'].required = True
        self.fields['delivery_address'].label = _('Delivery address')
        self.fields['promocode'].label = _('Promocode')
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
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput
                                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 1
        self.fields['quantity'].widget.attrs['style'] = 'width:80px; height:40px; padding-left:10px;'
