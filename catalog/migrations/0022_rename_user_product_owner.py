# Generated by Django 4.2.4 on 2023-09-18 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='owner',
        ),
    ]
