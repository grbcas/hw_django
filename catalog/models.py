from django.db import models

# Create your models here.
from django.db import models


NULLABLE = {'null': True, 'blank': True}


# Create your models here.
# class Student(models.Model):
#     first_name = models.CharField(max_length=100, verbose_name='name')
#     last_name = models.CharField(max_length=100, verbose_name='surname')
#     avatar = models.ImageField(upload_to='students/', verbose_name='avatar', **NULLABLE)
#
#     is_active = models.BooleanField(default=True, verbose_name='studies')
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'student'
#         verbose_name_plural = 'students'
#         ordering = ('last_name',)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='наименование'
    )
    description = models.TextField(
        max_length=200,
        verbose_name='описание'
    )
    # created_at = models.CharField(max_length=100, verbose_name='created_at', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return f'{self.pk, self.name}'


class Product(models.Model):
    name = models.CharField(
        'наименование',
        max_length=100,
        help_text='max 100 chars'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        help_text='max 100 chars'
    )
    description = models.TextField(
        max_length=200,
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='изображение',
        default='products/default.png',
        **NULLABLE
    )
    price = models.IntegerField(
        verbose_name='цена'
    )
    create_date = models.DateTimeField(
        verbose_name='дата создания'
    )
    modify_date = models.DateTimeField(
        verbose_name='дата изменения'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.pk} {self.name} {self.price} {self.category}'


class Contacts(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='названиеназвание'
    )

    class Meta:
        verbose_name = 'название'
        verbose_name_plural = 'названия'
        ordering = ('name',)

    def __str__(self):
        return f'{self.pk} {self.name}'
