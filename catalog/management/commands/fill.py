import datetime

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('truncate db')
        Product.objects.all().delete()

        products_list = [
            {'id': 5,
            'name': 'продукт-3',
            'category_id': 3,
            'description': 'продукт-3 Описание',
            'image': '6_factorial.drawio_XyqOlfo.png',
            'price': 3,
            'create_date': datetime.datetime(2023, 8, 20, 18, 18, 36, tzinfo=datetime.timezone.utc),
            'modify_date': datetime.datetime(2023, 8, 20, 18, 18, 43, tzinfo=datetime.timezone.utc)},
        ]

        products_to_db = []
        for i_product in products_list:
            products_to_db.append(
                Product(**i_product)
            )

        Product.objects.bulk_create(products_to_db)
