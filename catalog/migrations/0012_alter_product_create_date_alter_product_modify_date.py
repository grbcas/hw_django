# Generated by Django 4.2.4 on 2023-08-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_delete_student_alter_contacts_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modify_date',
            field=models.DateTimeField(verbose_name='дата изменения'),
        ),
    ]
