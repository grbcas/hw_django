# Generated by Django 4.2.4 on 2023-08-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_product_create_date_alter_product_modify_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_views',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
