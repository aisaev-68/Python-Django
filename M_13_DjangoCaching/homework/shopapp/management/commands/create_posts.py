import os
import random
import uuid
from pathlib import Path

from django.utils.timezone import now
from mimesis import Text, Internet
from mimesis.locales import Locale
import requests
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from blogs.models import Post, PostImage



new_dir_file = now().date().strftime("%Y/%m/%d")
uploaded_file_path = Path().parent / "media/post_images" / new_dir_file
uploaded_file_path.mkdir(exist_ok=True, parents=True)
uploaded_file_path = uploaded_file_path.absolute()

class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **options):
        self.stdout.write("Create posts")
        users = [user for user in User.objects.all()]

        for _ in range(20):
            user = random.choice(users)
            text = Text(locale=Locale.RU)
            internet = Internet()

            url = internet.stock_image(width=1920, height=1080)
            request = requests.get(url)
            filename = str(uuid.uuid4())
            file_name = "{name}.{ext}".format(name=filename, ext='jpg')
            file_path = "post_images/{new_dir}/{image_name}".format(new_dir=new_dir_file, image_name=file_name)
            path_absolute = str(Path(uploaded_file_path, file_name))
            with open(path_absolute, 'wb') as f:
                f.write(request.content)

            post = Post.objects.create(
                title=text.title(),
                description=text.text(),
                created_by=user,
            )
            post_image = PostImage(
                post=post,
                image=file_path,
            )
            post_image.save()

        self.stdout.write(self.style.SUCCESS("Posts created"))
