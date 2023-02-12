from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _
from shopapp.models import Profile


class RegisterUser(UserCreationForm, forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label=_("Повторный пароль"),
        widget=forms.PasswordInput(),
    )
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(),
    )

    city = forms.CharField(
        label='Город',
        widget=forms.TextInput(),
    )

    error_messages = {
        "password_mismatch": _("Пароли не совпадают!."),
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = 'username', 'password1', 'password2', 'phone', 'city'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['phone', 'city']
        widgets = {
            'phone': TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер телефона'}),
            'city': TextInput(attrs={'class': 'form-input', 'placeholder': 'Город'}),
        }



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Пользователь', widget=forms.TextInput(
            attrs={
                "autofocus": True,
                'class': 'form-input',
                'placeholder': 'Пользователь',
                'help_text': ''
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Пароль',
                'help_text': ''
            }
        )
    )
    password2 = forms.CharField(
        label='Повторный пароль', widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Повторный пароль',
                'help_text': ''
            }
        )
    )
    error_messages = {
        "password_mismatch": _("Пароли не совпадают!."),
    }

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileRegistrationForm(forms.ModelForm):
    phone = forms.CharField(
        label='Номер телефона', widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Номер телефона',
                'help_text': ''
            }
        )
    )
    city = forms.CharField(
        label='Город', widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Город',
                'help_text': ''
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('phone', 'city')
