import random

from django.core.management.base import BaseCommand

from mimesis import Address, Finance
from mimesis.locales import Locale
from django.utils.translation import gettext_lazy as _

from houseroom.models import HouseRoom


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create house")

        for _ in range(20):
            developer = Finance(locale=Locale.RU).company()
            city = Address(locale=Locale.RU).city()
            address = Address(locale=Locale.RU).address()
            HouseRoom.objects.create(
                city=city,
                address=address,
                developer=developer,
                floors=random.randint(1, 15),
            )
        self.stdout.write("Created houses")