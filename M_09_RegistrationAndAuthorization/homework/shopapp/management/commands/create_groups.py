from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission

from shopapp.models import Product, Order


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

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

            elif perm.codename == "change_product":
                editor_group.permissions.add(perm)

            elif perm.codename == "view_product":
                editor_group.permissions.add(perm)
                publisher_group.permissions.add(perm)
                clients_group.permissions.add(perm)

            elif perm.codename == "delete_product":
                cleaner_group.permissions.add(perm)

        content_type_order = ContentType.objects.get_for_model(Order)
        order_permission = Permission.objects.filter(content_type=content_type_order)
        for perm in order_permission:
            moderator_group.permissions.add(perm)
            editor_group.permissions.add(perm)
            publisher_group.permissions.add(perm)
            cleaner_group.permissions.add(perm)
            clients_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Groups created"))

        super_user = User.objects.create_superuser(username='admin', email='admin@ya.ru', password='12345')
        moderator_group = Group.objects.get(name="Moderator")
        super_user.groups.add(moderator_group)

        self.stdout.write(self.style.SUCCESS(f"{super_user} added in Moderator group"))

        editor_user = User.objects.create_user(username='editor', email='editor@ya.ru', password='aisa2002')
        editor_group = Group.objects.get(name="Editor")
        editor_user.groups.add(editor_group)

        self.stdout.write(self.style.SUCCESS(f"{editor_user} added in Editor group"))

        client_user = User.objects.create_user(username='client', email='client@ya.ru', password='aisa2002')
        client_group = Group.objects.get(name="Clients")
        client_user.groups.add(client_group)

        self.stdout.write(self.style.SUCCESS(f"{client_user} added in Clients group"))

        self.stdout.write(self.style.SUCCESS("Process end successful."))
