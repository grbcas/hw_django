# Generated by Django 4.2.4 on 2023-08-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_create_date_alter_product_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(verbose_name='дата создания'),
        ),
    ]
