import json
import os

from django.core.management import BaseCommand

from shopapp.models import Catalog, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(
                f"Start added category"
            )
        )
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        with open(os.path.join(BASE_DIR, 'commands/json_data.json')) as json_file:
            data = json.load(json_file)

        for catalog in data['data']:
            for name_catalog, catalogs in catalog.items():
                id_catalog = Catalog.objects.create(name=name_catalog)
                for group_name in catalogs.keys():
                    Category.objects.create(name=group_name, category=id_catalog)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added category"
            )
        )
