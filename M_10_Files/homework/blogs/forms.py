from django.forms.models import ModelForm
from django import forms
from .models import Post, PostImage


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Post
        fields = ["title", "description", ]


class PostImageForm(ModelForm):
    image = forms.ImageField(
        label="Изображение",
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = PostImage
        fields = ["image", ]


class SendMessageForm(forms.Form):
    first_name = forms.CharField(
        label='Имя*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )
    email = forms.EmailField(
        label="Email*",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        required=True
    )
    phone = forms.CharField(
        label='Номер телефона*',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
            },
        ),
        required=True
    )
    message = forms.CharField(
        label='Сообщение*',
        widget=forms.Textarea,
        max_length=2000,
        required=True,
    )
