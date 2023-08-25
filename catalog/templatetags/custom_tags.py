from django import template
from django.db import models
from config import settings

register = template.Library()


@register.simple_tag
def mediapath(object: models.Model) -> str:
    """Шаблонный тег для построения пути к медиафайлам приложения"""
    image_link = object.image
    if image_link:
        return f'{settings.MEDIA_URL}{image_link}'
    return f'{settings.MEDIA_URL}default.png'


@register.filter
def mediapath(object: models.Model) -> str:
    """Шаблонный фильтр для построения пути к медиафайлам приложения"""
    image_link = object.image
    if image_link:
        return f'{settings.MEDIA_URL}{image_link}'
    return f'{settings.MEDIA_URL}default.png'
