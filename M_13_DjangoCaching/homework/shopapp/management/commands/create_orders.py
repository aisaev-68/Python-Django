from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="admin")
        products = Product.objects.all()[:2]
        order = Order.objects.get_or_create(
            delivery_address="ul Pupkina, d 8",
            promocode="SALE123",
            user=user,
        )
        self.stdout.write(f"Created order {order}")
