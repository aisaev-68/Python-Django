from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from homework import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        # The magic line
        User.objects.create_user(
            username=settings.USERNAME,
            email=settings.EMAIL,
            password=settings.PASSWORD,
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
