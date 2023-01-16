import csv

from django.core.management.base import BaseCommand, CommandError

import shopapp.models as models


class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_products(self):
        with open("products.csv", encoding='utf-8', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            try:
                getattr(models, 'Product').get_or_create(**row)
            except AttributeError as error:
                print('Модели нет')
                break
