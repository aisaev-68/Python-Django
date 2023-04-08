from pathlib import Path

from django.utils.timezone import now
from mimesis import Address, Finance
from mimesis.locales import Locale
from django.core.management import BaseCommand


from shopapp.models import Shop

# new_dir_file = now().date().strftime("%Y/%m/%d")
# uploaded_file_path = Path().parent / "media/profile_images" / new_dir_file
# uploaded_file_path.mkdir(exist_ok=True, parents=True)
# uploaded_file_path = uploaded_file_path.absolute()


class Command(BaseCommand):
    """
    Creates shop
    """

    def handle(self, *args, **options):
        self.stdout.write("Create shops")

        for _ in range(20):
            shop_name = Finance(locale=Locale.RU)
            address = Address(locale=Locale.RU)

            Shop.objects.create(
                shop_name=shop_name.company(),
                address=address.address(),
            )

        self.stdout.write(self.style.SUCCESS("Shops created"))
