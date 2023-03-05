from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from PIL import Image



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))


    def __str__(self):
        return "Post {title}".format(title=self.title)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["title", "description"]


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts', verbose_name=_('Post'))
    image = models.FileField(upload_to="post_image/", blank=True, verbose_name=_('Files post'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 850 or img.width > 450:
            img.thumbnail((850, 450))
        img.save(self.image.path, quality=70, optimize=True)

    def __str__(self):
        return "PostImage {image}".format(image=self.image)

    class Meta:
        verbose_name = _("PostImage")
        verbose_name_plural = _("PostImages")
        ordering = ["post"]