from django import forms
from django.utils.translation import gettext_lazy as _



class ContactForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), )
    last_name = forms.CharField(label=_("Last name"), )
    email = forms.EmailField(label="Email", )
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'rows': 3, 'cols': 20,}))


