from django.core.management import BaseCommand
from django.db import models, connection, transaction
from django.apps import apps


class Command(BaseCommand):

    @staticmethod
    def clear_db(models: tuple[models.Model]) -> None:
        """Вспомогательный метод, предназначенный для очищения таблиц в базе данных"""

        with transaction.atomic():
            for model in models:
                model.objects.all().delete()

    @staticmethod
    def reset_sequence(models: tuple[models.Model]) -> None:
        """Вспомогательный метод, предназначенный для сброса счетчика автоинкремента в базе данных"""

        for model in models:
            table_name = model._meta.db_table
            sequence_name = f"{table_name}_id_seq"
            with connection.cursor() as cursor:
                cursor.execute(f"ALTER SEQUENCE {sequence_name} RESTART WITH 1;")
                connection.commit()

    def handle(self, *args, **options) -> None:
        """Основное действие команды.

        1) Очищает базу данных
        2) Сбрасывает счетчик автоинкремента
        3) заполняет базу данных новыми данными из файлов
        """

        app_name = self.__module__.split('.')[0]
        app_config = apps.get_app_config(app_name)
        models_ = tuple(app_config.get_models())

        # очищаем старые значения БД и сбрасываем счетчик
        self.clear_db(models_)
        self.reset_sequence(models_)
