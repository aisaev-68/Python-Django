from django.core.management import BaseCommand

from shopapp.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(
                f"Start added category"
            )
        )

        for category in lst_categories:
            Category.objects.create(name=category)


        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added category"
            )
        )