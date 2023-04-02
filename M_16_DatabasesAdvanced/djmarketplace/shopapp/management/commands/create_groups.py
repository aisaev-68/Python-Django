from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from mimesis import Person, Address
from mimesis.locales import Locale
from mimesis.enums import Gender
from django.utils.translation import gettext_lazy as _

from app_users.models import Profile
from product.models import Product
from order.models import Order


class Command(BaseCommand):
    help = _('Creates read only default permission groups for users')

    def handle(self, *args, **options):
        self.stdout.write("Create groups")
        moderator_group, created = Group.objects.get_or_create(name="Moderator")

        editor_group, created = Group.objects.get_or_create(name="Editor")
        publisher_group, created = Group.objects.get_or_create(name="Publisher")
        cleaner_group, created = Group.objects.get_or_create(name="Cleaner")
        clients_group, created = Group.objects.get_or_create(name="Clients")

        content_type_product = ContentType.objects.get_for_model(Product)
        product_permission = Permission.objects.filter(content_type=content_type_product)
        for perm in product_permission:
            moderator_group.permissions.add(perm)
            if perm.codename == "add_product":
                publisher_group.permissions.add(perm)
                editor_group.permissions.add(perm)

            elif perm.codename == "change_product":
                editor_group.permissions.add(perm)

            elif perm.codename == "view_product":
                editor_group.permissions.add(perm)
                publisher_group.permissions.add(perm)
                clients_group.permissions.add(perm)

            elif perm.codename == "delete_product":
                cleaner_group.permissions.add(perm)
                editor_group.permissions.add(perm)

        content_type_order = ContentType.objects.get_for_model(Order)
        order_permission = Permission.objects.filter(content_type=content_type_order)
        for perm in order_permission:
            moderator_group.permissions.add(perm)
            editor_group.permissions.add(perm)
            publisher_group.permissions.add(perm)
            cleaner_group.permissions.add(perm)
            clients_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Groups created"))
        person = Person(locale=Locale.RU)
        address = Address(locale=Locale.RU)
        super_user = User.objects.create_superuser(
            username='admin',
            first_name='Петр',
            last_name='Петрович',
            email='admin@ya.ru',
            password='12345')

        Profile.objects.create(
            user=super_user,
            postal_code=address.postal_code(),
            country=address.country(),
            city=address.city(),
            address=address.address(),
            phone=person.telephone(),
        )
        moderator_group = Group.objects.get(name="Moderator")
        super_user.groups.add(moderator_group)
        self.stdout.write(self.style.SUCCESS(f"{super_user} added in Moderator group"))

        person = Person(locale=Locale.RU)
        address = Address(locale=Locale.RU)
        editor_user = User.objects.create_user(
            username='editor',
            first_name='Борис',
            last_name='Борисович',
            email='editor@ya.ru',
            password='12345')

        Profile.objects.create(
            user=editor_user,
            postal_code=address.postal_code(),
            country=address.country(),
            city=address.city(),
            address=address.address(),
            phone=person.telephone(),
        )
        editor_group = Group.objects.get(name="Editor")
        editor_user.groups.add(editor_group)

        self.stdout.write(self.style.SUCCESS(f"{editor_user} added in Editor group"))

        for _ in range(20):
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
            client_group = Group.objects.get(name="Clients")
            client_user.groups.add(client_group)

            self.stdout.write(self.style.SUCCESS(f"{client_user} added in Clients group"))

        self.stdout.write(self.style.SUCCESS("Process end successful."))
