import csv
import os

from django.core.management.base import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    help = 'Import data from csv file'

    def handle(self, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = f"{BASE_DIR}/commands/products.csv"
        print(file_path)
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                try:
                    Product.objects.get_or_create(**row) # (<Product: Product object (1)>, True)
                except AttributeError as error:
                    print(error)
                    break
