from django.core.management import BaseCommand

from shopapp.models import Category

lst_categories = ['Электроника', 'Одежда','Обувь', 'Дом и сад', 'Детские товары', 'Красота и здоровье','Бытовая техника',
       'Спорт и отдых', 'Строительсство и ремонт', 'Продукты питания','Аптека', 'Товраы для животных', 'Книги',
       'Туризм, рыбалка, охота','Автотовары', 'Хобби и творчество', 'Ювелирные украшения', 'Акцессуары','Игры и консоли',
       'Канцелярские товары', 'Цифровые товары', 'Антиквариат и коллекционирование','Бытовая химия и гигиена', 'Музыка и видео',
       'Электронные сигареты и товары для курения', ]
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