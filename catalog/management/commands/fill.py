import json
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Product


PATH = Path(__file__).parent.parent.parent.parent.joinpath('data.json')


class Command(BaseCommand):

    @staticmethod
    def load_json() -> list:
        """
        load data from fixture dumpdata
        :return: list
        """
        with open(PATH, 'r', encoding='cp1251') as f:
            dump_data = json.load(f)
            return dump_data

    def handle(self, *args, **options):
        """
        fill data into db
        :param args:
        :param options:
        :return:
        """
        print('fill data from fixture dumpdata')
        products_to_db = []
        for i_product in self.load_json():
            products_to_db.append(Product(**i_product))

        Product.objects.bulk_create(products_to_db)
