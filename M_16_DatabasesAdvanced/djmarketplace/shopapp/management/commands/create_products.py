import os
import random
import uuid
from pathlib import Path, PurePath

from django.contrib.auth.models import User
from django.core.management import BaseCommand
import requests
import json

from django.utils.timezone import now

from product.models import Product
from shopapp.models import Shop

new_dir_file = now().date().strftime("%Y/%m/%d")
uploaded_file_path = Path().parent / "media/product_images" / new_dir_file
uploaded_file_path.mkdir(exist_ok=True, parents=True)
uploaded_file_path = uploaded_file_path.absolute()


class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **options):

        self.stdout.write("Create products")
        with open(str(Path(__file__).parent.joinpath('json_data-products.json'))) as json_file:
            data = json.load(json_file)

        user = User.objects.filter(username='editor').first()
        shops = [s.pk for s in Shop.objects.all()]

        for d in data["data"]:
            start_numb = random.choices([1, 4, 2, 4, 4, 3, 4])[0]
            end_numb = random.choices([5, 6, 5, 5])[0]
            shop = shops[start_numb:end_numb]

            request = requests.get(d['image'])
            shop = shops[start_numb:end_numb]
            filename = str(uuid.uuid4())
            file_name = "{name}.{ext}".format(name=filename, ext='jpg')
            file_path = "product_images/{new_dir}/{image_name}".format(new_dir=new_dir_file, image_name=file_name)
            path_absolute = str(Path(uploaded_file_path, file_name))
            with open(path_absolute, 'wb') as f:
                f.write(request.content)

            product = Product.objects.create(
                name=d['name'],
                brand="Apple",
                description=d['description'],
                attributes=d['attributes'],
                rating=d.get('rating'),
                created_by=user,
                price=d['price'],
                discount=random.choices([5, 10, 15, 20])[0],
                image=file_path,
                products_count=50,
                sold=random.choices([x + 1 for x in range(50)])[0],
                archived=False,
            )
            if len(shop) == 1:
                product.shop.add(shop[0])
            elif len(shop) == 2:
                product.shop.add(shop[0], shop[1])
            elif len(shop) == 3:
                product.shop.add(shop[0], shop[1], shop[2])
            elif len(shop) == 4:
                product.shop.add(shop[0], shop[1], shop[2], shop[3])
            elif len(shop) == 5:
                product.shop.add(shop[0], shop[1], shop[2], shop[3], shop[4])



        self.stdout.write(self.style.SUCCESS("Products created"))
