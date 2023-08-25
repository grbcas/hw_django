from django import template
from django.db import models
from config import settings
from catalog.models import Product

register = template.Library()


@register.simple_tag
def mediapath(object: models.Model) -> str:
    """Шаблонный тег для построения пути к медиафайлам приложения"""

    print('register.simple_tag', hasattr(object, 'image'))
    if hasattr(object, 'image'):
        print(settings.MEDIA_URL)
        return f'{settings.MEDIA_URL}/{object}'
    return f'{settings.MEDIA_URL}default.png'


@register.filter
def mediapath(object: models.Model) -> str:
    """Шаблонный фильтр для построения пути к медиафайлам приложения"""
    print('@register.filter')
    object_image = Product.image
    if object_image:
        return f'{settings.MEDIA_URL}/{object_image}'
    return f'{settings.MEDIA_URL}default.png'
