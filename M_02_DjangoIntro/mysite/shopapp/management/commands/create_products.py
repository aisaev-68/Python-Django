import csv

from django.core.management.base import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    help = 'Import data from csv file'

    # def add_arguments(self, parser):
    #     parser.add_argument('name', type=str)
    #     parser.add_argument('description', type=str)
    #     parser.add_argument('price', type=float)

    def handle(self, *args, **options):
        # name = options['name']
        # description = options['description']
        # price = options['price']
        with open("commands/products.csv", encoding='utf-8', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            try:
                Product.objects.get_or_create(**row)
            except AttributeError as error:
                print('Модели нет')
                break
