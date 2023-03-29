import decimal
import os
import random
import uuid
from pathlib import Path, PurePath

from django.contrib.auth.models import User
from django.core.management import BaseCommand
import requests
import json

from django.utils.timezone import now

from product.models import Product, ShopItem
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
        # with open(str(Path(__file__).parent.joinpath('json_data-products.json'))) as json_file:
        #     data = json.load(json_file)
        #
        # user = User.objects.filter(username='editor').first()
        # shops = [s.pk for s in Shop.objects.all()]
        # for key, value in data.items():
        #     start_numb = random.choices(range(1, 11))[0]
        #     end_numb = random.choices(range(11, 21))[0]
        #     shop = shops[start_numb:end_numb]
        #
        #     for d in value:
        #
        #         request = requests.get(d['image'][0])
        #         filename = str(uuid.uuid4())
        #         file_name = "{name}.{ext}".format(name=filename, ext='jpg')
        #         file_path = "product_images/{new_dir}/{image_name}".format(new_dir=new_dir_file, image_name=file_name)
        #         path_absolute = str(Path(uploaded_file_path, file_name))
        #         with open(path_absolute, 'wb') as f:
        #             f.write(request.content)
        #
        #         product = Product.objects.create(
        #             name=d['name'],
        #             brand=key,
        #             description=d['description'],
        #             attributes=d['attributes'],
        #             rating=d.get('rating'),
        #             created_by=user,
        #             price=decimal.Decimal(d['price']),
        #             discount=d['discount'],
        #             image=file_path,
        #             products_count=50,
        #             sold=d['sold'],
        #             archived=d['archived'],
        #         )
        #         for s in shop:
        #             ShopItem.objects.create(shop_id=s, product_id=product.pk)
        #
        #         self.stdout.write(self.style.SUCCESS(f"Product {product} add"))
        import itertools

        pks_to_delete = []
        rows = Product.objects.values_list('pk', 'name').order_by('name')
        filter_func = lambda x: x[1]
        for key, group in itertools.groupby(rows.iterator(), filter_func):
            pks_to_delete.extend((i[0] for i in list(group)[1:]))

        Product.objects.filter(pk__in=pks_to_delete).delete()
        self.stdout.write(self.style.SUCCESS("Products created"))
