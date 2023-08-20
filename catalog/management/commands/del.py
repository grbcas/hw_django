from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        truncate data in a db
        :param args:
        :param options:
        :return:
        """
        print('truncate product to db')
        Product.objects.all().delete()
