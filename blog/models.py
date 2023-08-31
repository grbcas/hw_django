from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='title',
    )
    body = models.TextField(
        max_length=100,
        verbose_name='content',
        **NULLABLE
    )
    slug = models.CharField(
        max_length=50,
        verbose_name='slug',
    )
    image = models.ImageField(
        verbose_name='image',
        **NULLABLE
    )
    create_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='creation date',
    )
    modify_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='modification date',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
