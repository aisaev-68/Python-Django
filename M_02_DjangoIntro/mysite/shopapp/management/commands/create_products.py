import csv
import os

from django.core.management.base import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    help = 'Import data from csv file'

    # def add_arguments(self, parser):
    #     parser.add_argument('name', type=str)
    #     parser.add_argument('description', type=str)
    #     parser.add_argument('price', type=float)

    def handle(self, *args, **kwargs):
        # name = options['name']
        # description = options['description']
        # price = options['price']

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = f"{BASE_DIR}/commands/products.csv"
        print(file_path)
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                try:

                    Product.objects.get_or_create(**row)

                except AttributeError as error:
                    print('Модели нет')
                    break
