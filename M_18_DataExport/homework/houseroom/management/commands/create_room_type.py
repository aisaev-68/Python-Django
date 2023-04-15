from django.core.management.base import BaseCommand, CommandError

from houseroom.models import RoomType, NumberRoom


class Command(BaseCommand):

    def handle(self, *args, **options):
        # The magic line
        self.stdout.write("Start create room type.")
        for item in ["Студия", "Квартира", "Пентхаус"]:
            RoomType.objects.create(
                type_name=item
            )

        for item in range(5):
            NumberRoom.objects.create(
                room_count=item + 1
            )

        self.stdout.write("Create room type.")