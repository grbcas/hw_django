# Generated by Django 4.2.4 on 2023-08-19 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('last_name',), 'verbose_name': 'student', 'verbose_name_plural': 'students'},
        ),
    ]
