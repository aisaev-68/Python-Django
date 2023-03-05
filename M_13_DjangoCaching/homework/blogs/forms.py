from django.forms.models import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Post, PostImage


class PostForm(ModelForm):
    title = forms.CharField(
        label=_("Title"),
        required=True,
        widget=forms.TextInput(attrs={})
    )
    description = forms.FileField(
        label=_("Post"),
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 20})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Post
        fields = ["title", "description", ]


class PostImageForm(ModelForm):
    images = forms.FileField(
        label=_("Image post"),
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = PostImage
        fields = ["images", ]


class SendMessageForm(forms.Form):
    first_name = forms.CharField(
        label=_('First name*'),
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )
    email = forms.EmailField(
        label=_("Email*"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        required=True
    )
    phone = forms.CharField(
        label=_('Phone*'),
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
            },
        ),
        required=True
    )
    message = forms.CharField(
        label=_('Message*'),
        widget=forms.Textarea,
        max_length=2000,
        required=True,
    )
