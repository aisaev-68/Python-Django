import decimal
import os
import random
import uuid
from pathlib import Path, PurePath
import itertools
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
        with open(str(Path(__file__).parent.joinpath('json_data-products.json'))) as json_file:
            data = json.load(json_file)["data"]
        prod_len = len(data)
        user = User.objects.filter(username='editor').first()
        shops = [s.pk for s in Shop.objects.all()]

        for value in data:
            start_shop = sorted(random.sample(shops, 3))
            request = requests.get(value.get('image')[0])
            filename = str(uuid.uuid4())
            file_name = "{name}.{ext}".format(name=filename, ext='jpg')
            file_path = "product_images/{new_dir}/{image_name}".format(new_dir=new_dir_file,
                                                                       image_name=file_name)
            path_absolute = str(Path(uploaded_file_path, file_name))
            with open(path_absolute, 'wb') as f:
                f.write(request.content)

            discount = value.get('discount')
            price = decimal.Decimal(value.get('price'))
            new_price = (price - price * discount / 100)

            product = Product.objects.create(
                        name=value.get('name'),
                        brand=value.get('brand'),
                        description=value.get('description'),
                        attributes=value.get('attributes'),
                        rating=value.get('rating'),
                        created_by=user,
                        price=price,
                        new_price=new_price,
                        discount=discount,
                        image=file_path,
                        products_count=50,
                        sold=value.get('sold'),
                        archived=value.get('archived'),
                    )
            for idx in start_shop:
                ShopItem.objects.create(shop_id=idx, product_id=product.pk)

            self.stdout.write(self.style.SUCCESS(f"Product {product} created"))




        # pks_to_delete = []
        # rows = Product.objects.values_list('pk', 'name').order_by('name')
        # filter_func = lambda x: x[1]
        # for key, group in itertools.groupby(rows.iterator(), filter_func):
        #     pks_to_delete.extend((i[0] for i in list(group)[1:]))
        #
        # Product.objects.filter(pk__in=pks_to_delete).delete()
        self.stdout.write(self.style.SUCCESS("Products created"))
