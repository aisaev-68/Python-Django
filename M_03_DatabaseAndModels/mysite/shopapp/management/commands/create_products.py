import csv
import os

from django.core.management.base import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    help = 'Добавление продукции'

    def handle(self, *args, **options):
        self.stdout.write("Добавление продукции")
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
        self.stdout.write(self.style.SUCCESS("Продукция добавлена"))