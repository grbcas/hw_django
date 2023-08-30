# Create your models here.
from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='наименование'
    )
    description = models.TextField(
        max_length=200,
        verbose_name='описание'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


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
        default='default.png',
        upload_to='products/',
        verbose_name='изображение',
    )
    price = models.IntegerField(
        verbose_name='цена'
    )
    create_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата создания'
    )
    modify_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата изменения'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано'
        )
    count_views = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров'
        )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        verbose_name='slug',
        **NULLABLE
        )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.pk} {self.name} {self.price} {self.category} {self.is_published}'


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
