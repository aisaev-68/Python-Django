from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from homework import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        # The magic line

        User.objects.create_superuser(
            username=settings.USER_ADMIN,
            email=settings.EMAIL,
            password=settings.PASSWORD,
        )
