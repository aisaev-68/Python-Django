import json
import random
from email._header_value_parser import ContentType

from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from django.test import TestCase
from mimesis import Address, Person
from mimesis.enums import Locale, Gender

from accounts.models import Profile
from shopapp.models import Product, Order


def get_promo_code(num: int):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code


class OrderDetailTestCase(TestCase):
    fixtures = ['groups-fixtures.json', 'users-fixtures.json', 'profiles-fixtures.json', 'products-fixtures.json', ]

    @classmethod
    def setUpClass(cls):
        # Установки запускаются 1 раз перед тестами
        """
        Выборка пользователя и продуктов
        """
        super().setUpClass()

        cls.user = User.objects.get(pk=15)
        cls.products = Product.objects.filter(archived=False)

    def setUp(self) -> None:
        """
        Вход пользователя и создание заказа для дальнейшего теста.
        """

        address = Address(locale=Locale.RU)
        delivery_address = address.country(), address.postal_code(), address.city(), address.address()
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            delivery_address=delivery_address,
            promocode=get_promo_code(num=20),
            user=self.user,
        )
        self.order.products.set(self.products[3:6])

    def tearDown(self) -> None:
        """
        Удаление заказа.
        """
        self.order.delete()

    def test_order_details(self):
        """
        Тест проверяет
         - проверка получения заказа:
         - наличие в теле ответа адреса заказа;
         - наличие в теле ответа промокода;
         - наличие в контексте ответа того же заказа, который был создан;
         - перед тестом (сравнение заказов по первичному ключу).
        """

        response = self.client.get(
            reverse('shopapp:order_detail',
                    args=[self.order.pk]),
        )
        self.assertEqual(response.context['orders'].pk, self.order.pk)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['orders'].delivery_address)
        self.assertTrue(response.context['orders'].promocode)
        self.assertEqual(response.context['orders'], self.order)





class OrdersExportTestCase(TestCase):
    fixtures = ['groups-fixtures.json', 'users-fixtures.json', 'profiles-fixtures.json', 'products-fixtures.json', 'orders-fixtures.json',]
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        person = Person(locale=Locale.RU)
        address = Address(locale=Locale.RU)

        cls.user = User.objects.create_user(
            username=person.username(),
            first_name=person.first_name(gender=Gender.MALE),
            last_name=person.last_name(gender=Gender.MALE),
            email=person.email(),
            password='12345',
            is_staff=True,

        )
        # Profile.objects.create(
        #     user=cls.user,
        #     postal_code=address.postal_code(),
        #     country=address.country(),
        #     city=address.city(),
        #     address=address.address(),
        #     phone=person.telephone(),
        # )



    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)



    def tearDown(self) -> None:
        pass

    def test_orders_export(self):
        response = self.client.get(
            reverse('shopapp:orders_export')
        )


        # print(response.json())
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(response.context['all-orders'])
        # self.assertTrue(response.context['orders'].promocode)
        # self.assertEqual(response.context['orders'], self.order)