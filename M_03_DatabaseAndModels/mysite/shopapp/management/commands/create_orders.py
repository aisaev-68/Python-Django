import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Product, Order


class Command(BaseCommand):
    help = 'Добавление заказов'

    def handle(self, *args, **options):
        self.stdout.write("Добавление заказов")
        add_users()
        orders_dict = [
            {
                "promocode": 123555,
                "delivery_address": "Moscow",
                "user": User(id=2),
            },
            {
                "promocode": 123543,
                "delivery_address": "Moscow",
                "user": User(id=2),
            },
            {
                "promocode": 123523,
                "delivery_address": "Paris",
                "user": User(id=3),
            },
            {
                "promocode": 123521,
                "delivery_address": "Paris",
                "user": User(id=3),
            },
        ]

        for ind, order_item in enumerate(orders_dict):
            product = Product.objects.get(id=ind + 1)
            try:
                order = Order.objects.get_or_create(**order_item)
                order[0].product.add(product)
            except AttributeError as error:
                print(error)
                break
        self.stdout.write(self.style.SUCCESS("Заказы добавлены"))


def add_users():
    users = [
        {
            "username": "Bob",
            "email": "bob@ya.com",
            "password": "asdas1",
        },
        {
            "username": "Tom",
            "email": "tom@ya.com",
            "password": "asdas2",
        },
        {
            "username": "Jon",
            "email": "jon@ya.com",
            "password": "asdas3",
        },
    ]
    for user in users:
        User.objects.create_user(**user)
