import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Product, Order





class Command(BaseCommand):
    help = 'Add data in Order'

    def handle(self, *args, **options):
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
        id_product = [1, 2, 3, 4]
        for order_item in orders_dict:
            order = Order.objects.get_or_create(**order_item)
            order.product.get_or_create(random.choice(id_product))



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