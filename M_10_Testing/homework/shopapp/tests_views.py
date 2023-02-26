import random

from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.test import TestCase
from mimesis import Person, Address
from mimesis.enums import Locale, Gender
from accounts.models import Profile
from shopapp.models import Product


def get_promo_code(num: int):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code


class OrderDetailTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # Установки запускаются перед каждым тестом
        person = Person(locale=Locale.RU)
        address = Address(locale=Locale.RU)
        cls.user = User.objects.create_user(
            username=person.username(),
            first_name=person.first_name(gender=Gender.MALE),
            last_name=person.last_name(gender=Gender.MALE),
            email=person.email(),
            password='12345',

        )
        Profile.objects.create(
            user=cls.user,
            postal_code=address.postal_code(),
            country=address.country(),
            city=address.city(),
            address=address.address(),
            phone=person.telephone(),
        )
        group = Group.objects.get(name="Clients")
        cls.user.groups.add(group)

    @classmethod
    def tearDownClass(cls):
        # Очистка после каждого метода
        cls.user.delete()
        # cls.profile.delete()

    def setUp(self) -> None:
        # вход пользователя и создание заказа для дальнейшего теста
        address = Address(locale=Locale.RU)
        delivery_address = address.country(), address.postal_code(),address.city(), address.address()
        self.client.force_login(self.user)
        self.client.post(
            reverse('shopapp:create_order'),
            {
                'delivery_address': delivery_address,
                'promocode': get_promo_code(num=20),
                'user': self.user,
                'products': [p.pk for p in Product.objects.filter(archived=False).all() if p.pk < 5],

            }
        )

    def tearDown(self) -> None:
        # удаление заказа
        pass


    def test_order_details(self):
        # проверка получения заказа:
        # убедитесь, что в теле ответа есть адрес заказа;
        # убедитесь, что в теле ответа есть промокод;
        # убедитесь, что в контексте ответа тот же заказ, который был создан
        # перед тестом(сравните по первичному ключу).
        response = self.client.get(
            reverse('shopapp:order_detail'),
        )