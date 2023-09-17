from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email address')
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='phone', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='country', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='is_verified')
    verification_key = models.PositiveSmallIntegerField(verbose_name='verification_key', **NULLABLE)

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
