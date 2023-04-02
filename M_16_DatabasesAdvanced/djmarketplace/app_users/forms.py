from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import HiddenInput
from django.utils.translation import gettext_lazy as _
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        label=_("Username"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('User*'),
                'help_text': ''
            }
        ),
        required=True
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password*'),
                'help_text': ''
            }
        ),
        required=True
    )


class UserFormUpdate(forms.ModelForm):
    first_name = forms.CharField(
        label=_("First name*"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('First name*'),
            }
        ),
        required=True
    )
    last_name = forms.CharField(
        label=_("Last name*"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Last name*'),
            }
        ),
        required=True
    )

    email = forms.EmailField(
        label=_("Email*"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'placeholder': _('Email*'),
        }
        ),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]


class UserForm(UserFormUpdate, forms.ModelForm):
    username = forms.CharField(
        label=_("Username*"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('User*'),
            }
        ),
        required=True
    )
    password1 = forms.CharField(
        label=_("Password*"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': _('Password*'),
                'help_text': ''
            }
        ),
        required=True,
    )
    password2 = forms.CharField(
        label=_("Repeat password*"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': _('Repeat password*'),
                'help_text': ''
            }
        ),
        required=True,
    )

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password no match')
        return cd['password1']

    class Meta:
        model = User
        fields = ["username", "password1", "password2", 'first_name', 'last_name', 'email', ]


class ProfileForm(forms.ModelForm):
    country = forms.CharField(
        label=_("Country*"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Country*'),
            }
        ),
        required=True
    )
    postal_code = forms.CharField(
        label=_('Postal code'),
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Postal code'),
            }
        ),
        required=False
    )
    city = forms.CharField(
        label=_("City"),
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('City'),
            }
        ),
        required=False
    )
    address = forms.CharField(
        label=_("Address"),
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Address'),
            }
        ),
        required=False
    )

    phone = forms.CharField(
        label=_("Phone*"),
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                'placeholder': _('Phone*'),
            },
        ),
        required=True
    )
    avatar = forms.ImageField(
        label=_("Avatar"),
        required=False,
        widget=forms.FileInput(
            attrs={
                'placeholder': _('Avatar'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget = HiddenInput()
        self.fields['status'].label = ''
        # self.fields["status"].widget.attrs = {'readonly': 'readonly'}
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            # self.fields[field].label = ''

    class Meta:
        model = Profile
        fields = ['avatar', 'country', 'postal_code', 'city', 'address', 'phone', "status"]
