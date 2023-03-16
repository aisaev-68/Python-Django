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

        with open(os.path.join(BASE_DIR, 'commands/json_data-categories.json')) as json_file:
            data = json.load(json_file)

        for catalog in data['data']:
            for name_catalog, catalogs in catalog.items():
                rus_name, eng_name = name_catalog.split('-')
                id_catalog = Catalog.objects.create(name=rus_name, eng_name=eng_name)
                for name in catalogs.keys():
                    group_name, slug = name.split('-')
                    Category.objects.create(name=group_name, catalog=id_catalog, slug=slug.replace(', ', '-').replace(' ', '-'))

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added category"
            )
        )
