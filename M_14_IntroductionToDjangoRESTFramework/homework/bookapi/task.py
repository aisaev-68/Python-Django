# import random
#
# from faker import Faker
# from datetime import datetime
#
# fake = Faker('ru_RU')
#
# for _ in range(20):
#     # f.date_between_dates(date_start=datetime(2015, 1, 1), date_end=datetime(2019, 12, 31)).year)
#     # print(fake.first_name(), fake.last_name(), fake.isbn13(), fake.year())
#
#     # d = fake.date_between_dates(date_start=datetime(1950, 1, 1), date_end=datetime(2006, 12, 31)).year
#     # print(type(d))
#
#     first_name, last_name = random.choices([
#         (fake.first_name_male(), fake.last_name_male()),
#         (fake.first_name_female(), fake.last_name_female())
#     ])[0]
#     print(first_name, last_name)

from models import Book

print(Book.objects.first().__dict__)