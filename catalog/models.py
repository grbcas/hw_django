# Create your models here.
from users.models import User
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
        help_text='max 100 chars',
        unique=True
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
        **NULLABLE
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2
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
        default=True,
        verbose_name='Отображать'
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
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        **NULLABLE
    )

    def __str__(self):
        return f'{self.pk} {self.name} {self.price} {self.category} {self.is_published}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Contacts(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='названиеназвание'
    )

    def __str__(self):
        return f'{self.pk} {self.name}'

    class Meta:
        verbose_name = 'название'
        verbose_name_plural = 'названия'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        **NULLABLE
    )
    version_number = models.CharField(
        max_length=150,
        verbose_name='номер версии')
    version_name = models.CharField(
        max_length=150,
        verbose_name='название версии')
    version_sing = models.BooleanField(
        default=False,
        verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} Версия:{self.version_name}'

    class Meta:
        verbose_name = 'Версия_продукт'
        verbose_name_plural = 'Версия_продукты'
