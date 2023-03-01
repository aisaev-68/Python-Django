from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from mimesis import Person, Address
from mimesis.locales import Locale
from mimesis.enums import Gender

from myAuth.models import Profile


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        self.stdout.write("Create superuser")

        super_user = User.objects.create_superuser(
            username='admin',
            first_name='Петр',
            last_name='Петрович',
            email='admin@ya.ru',
            password='12345')
        self.stdout.write(self.style.SUCCESS(f"Created superuser {super_user}"))

        for _ in range(4):
            person = Person(locale=Locale.RU)
            address = Address(locale=Locale.RU)
            client_user = User.objects.create_user(
                username=person.username(),
                first_name=person.first_name(gender=Gender.MALE),
                last_name=person.last_name(gender=Gender.MALE),
                email=person.email(),
                password='12345',

            )
            Profile.objects.create(
                user=client_user,
                postal_code=address.postal_code(),
                country=address.country(),
                city=address.city(),
                address=address.address(),
                phone=person.telephone(),
            )

        self.stdout.write(self.style.SUCCESS("Process end successful."))
