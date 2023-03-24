from django import forms

class CartAddProductForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 0
        self.fields['quantity'].widget.attrs['style'] = 'width:80px; height:40px; padding-left:10px;'

    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput
                                )