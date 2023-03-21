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
            numb_author = random.choices([2, 3, 1, 2, 2, 1])[0]
            lst = []

            for _ in range(numb_author):

                first_name, last_name = random.choices([
                        (fake.first_name_male(), fake.last_name_male()),
                        (fake.first_name_female(), fake.last_name_female())
                    ])[0]

                lst.append(Author.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        year_birth=fake.date_between_dates(date_start=datetime(1950, 1, 1),
                                                           date_end=datetime(1980, 12, 31)).year
                    ))

            average_birth = sum([a.year_birth for a in lst]) // len(lst)
            book = Book.objects.create(
                    title=fake.text(max_nb_chars=50),
                    isbn=fake.isbn13(),
                    publication_date=random.randint(average_birth + 20, 2023),
                    pages=random.randint(100, 1500),
                )

            if len(lst) == 1:
                book.authors.add(lst[0])
            elif len(lst) == 2:
                book.authors.add(lst[0], lst[1])
            elif len(lst) == 3:
                book.authors.add(lst[0], lst[1], lst[2])



        self.stdout.write(self.style.SUCCESS("Process end successful."))