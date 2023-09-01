# Generated by Django 4.2.4 on 2023-08-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='name')),
                ('last_name', models.CharField(max_length=100, verbose_name='surname')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='avatar')),
            ],
            options={
                'verbose_name': 'name',
                'verbose_name_plural': 'names',
                'ordering': ('last_name',),
            },
        ),
    ]