import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from datetime import datetime


from django.utils.translation import gettext_lazy as _

from bookapi.models import Book, Author

fake = Faker('ru_RU')

class Command(BaseCommand):
    help = _('Creates read only default permission groups for users')

    def handle(self, *args, **options):
        self.stdout.write("Create superuser, authors and books")
        User.objects.create_superuser(
            username='admin',
            first_name='Петр',
            last_name='Петрович',
            email='admin@ya.ru',
            password='12345')

        for _ in range(5000):
            first_name, last_name = random.choices([
                (fake.first_name_male(), fake.last_name_male()),
                (fake.first_name_female(), fake.last_name_female())
            ])[0]
            author = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                year_birth=fake.date_between_dates(date_start=datetime(1950, 1, 1),
                                                   date_end=datetime(1990, 12, 31)).year

            )

            book = Book.objects.create(
                title=fake.text(max_nb_chars=50),
                isbn=fake.isbn13(),
                publication_date=random.randint(author.year_birth + 25, 2023),
                pages=random.randint(100, 1500),
            )
            book.authors.add(author)
            book.save()


        self.stdout.write(self.style.SUCCESS("Process end successful."))