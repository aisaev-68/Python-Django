from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))
    published = models.BooleanField(default=False, verbose_name=_('Published'))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ["title"]

    def __str__(self):
        return "News {t}".format(t=self.title)
