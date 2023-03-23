import os

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from PIL import Image


def get_upload_path_by_profiles(instance, filename):
    return os.path.join('post_images/', now().date().strftime("%Y/%m/%d"), filename)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles', verbose_name=_('User'))
    avatar = models.ImageField(upload_to=get_upload_path_by_profiles,
                               verbose_name=_('Avatar'),
                               null=True,
                               blank=True,
                               default='avatars/default_avatars.png')
    country = models.CharField(max_length=100, verbose_name=_('Country'), blank=True)
    postal_code = models.CharField(max_length=20, verbose_name=_('Postal code'), blank=True)
    city = models.CharField(max_length=100, verbose_name=_('City'), blank=True)
    address = models.CharField(max_length=200, verbose_name=_('Address'), blank=True)
    phone = models.CharField(max_length=20, db_index=True, verbose_name=_('Phone'), blank=True)
    balance = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name=_('Balance'))

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ["user", "address"]


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            img.thumbnail((100, 100))
        img.save(self.avatar.path, quality=70, optimize=True)