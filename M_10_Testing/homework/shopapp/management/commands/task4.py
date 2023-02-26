import os
import uuid
from pathlib import Path

import mimesis
from mimesis import Person, Address, Text, Internet, File
from mimesis.locales import Locale
from mimesis.enums import Gender
import requests
from django.conf import settings


person = Person(locale=Locale.RU)
address = Address(locale=Locale.RU)
text = Text(locale=Locale.RU)
internet = Internet()
file = File()

print(person.first_name(gender=Gender.MALE))
print(person.last_name(gender=Gender.MALE))
print(person.email())
print(person.telephone())
print(person.title())
print(address.country())
print(address.postal_code())
print(address.city())
print(address.address())
print(address.address())
print(text.title())
print(text.text())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
url = internet.stock_image(width=1920, height=1080)
filename = str(uuid.uuid4())
req = requests.get(url)
file_name = "{name}.{ext}".format(name=filename, ext='jpg')
file_path = "images/{image_name}".format(image_name=file_name)
path_absolute = str(Path('images/', file_name))
print(path_absolute)


with open(path_absolute, 'wb') as f:
    f.write(req.content)