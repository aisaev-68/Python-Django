from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserFormUpdate(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('First name*'),
            }
        ),
        required=True
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Last name*'),
            }
        ),
        required=True
    )

    email = forms.EmailField(
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
            self.fields[field].label = ''



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]


class UserForm(UserFormUpdate, forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('User*'),
            }
        ),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': _('Password*'),
                'help_text': ''
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': _('Repeat password*'),
                'help_text': ''
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''
            self.fields[field].label = ''

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password no match')
        return cd['password1']

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', ]


class ProfileForm(forms.ModelForm):
    country = forms.CharField(
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
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('City'),
            }
        ),
        required=False
    )
    address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Address'),
            }
        ),
        required=False
    )

    phone = forms.CharField(
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
        required=False,
        widget=forms.FileInput(
            attrs={
                'placeholder': _('Avatar'),
            }
        )
    )


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].label = ''


    class Meta:
        model = Profile
        fields = ['avatar', 'country', 'postal_code', 'city', 'address', 'phone']
