# Generated by Django 4.2.4 on 2023-08-20 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_student_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(max_length=200, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='max 100 chars', max_length=100, verbose_name='наименование')),
                ('description', models.TextField(max_length=200, verbose_name='описание')),
                ('image', models.ImageField(upload_to='', verbose_name='изображение')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('create_date', models.CharField(max_length=100, verbose_name='дата создания')),
                ('modify_date', models.DateTimeField(verbose_name='дата создания')),
                ('category', models.ForeignKey(help_text='max 100 chars', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
    ]
