import random
from decimal import Decimal
from django.core.management.base import BaseCommand

from mimesis import Address, Finance
from mimesis.locales import Locale
from django.utils.translation import gettext_lazy as _

from houseroom.models import HouseRoom, Room, NumberRoom, RoomType


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create house")
        numb_room = NumberRoom.objects.all()
        room_type = RoomType.objects.all()

        for _ in range(20):
            developer = Finance(locale=Locale.RU).company()
            city = Address(locale=Locale.RU).city()
            address = Address(locale=Locale.RU).address()
            house = HouseRoom.objects.create(
                city=city,
                address=address,
                developer=developer,
                floors=random.randint(1, 15),
            )

            for _ in range(70):
                Room.objects.create(
                    house=house,
                    storey=random.randint(1, house.floors),
                    total_area=float(random.choices([35, 45, 55, 67, 87, 90, 100, 120])[0]),
                    price=Decimal(random.choices([3500000, 4000000, 4500000, 5000000])[0]),
                    room_type=random.choices(room_type)[0],
                    room_number=random.choices(numb_room)[0],
                )
        self.stdout.write("Created houses")