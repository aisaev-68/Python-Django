from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from PIL import Image


def get_upload_path_by_posts(instance, filename):
    return os.path.join('post_images/', now().date().strftime("%Y/%m/%d"), filename)


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


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images', verbose_name=_('News'))
    image = models.FileField(upload_to=get_upload_path_by_posts, blank=True, verbose_name=_('Files post'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 850 or img.width > 450:
            img.thumbnail((850, 450))
        img.save(self.image.path, quality=70, optimize=True)

    def __str__(self):
        return "NewsImage {image}".format(image=self.image)

    class Meta:
        verbose_name = _("News image")
        verbose_name_plural = _("News images")
        ordering = ["news", ]