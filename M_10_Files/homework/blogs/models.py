from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True)
    created_by = models.ForeignKey(User, verbose_name='Кем создан', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return "Post {title}".format(title=self.title)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts', verbose_name='Пост')
    image = models.FileField(upload_to="post_image/", blank=True, verbose_name='Файлы поста')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1200 or img.width > 800:
            img.thumbnail((1200, 800))
        img.save(self.image.path, quality=70, optimize=True)

    def __str__(self):
        return "PostImage {image}".format(image=self.image)

    def to_json(self):
        posts = Post.objects.all()
        post_list = []
        for post in posts:
            image_post = {
                    'posts': post,
                    'images': PostImage.objects.filter(post_id=post.pk)
                }
            post_list.append(image_post)
        return post_list