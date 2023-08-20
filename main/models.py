from django.db import models


NULLABLE = {'null':True, 'blanl':True}

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='surname')
    avatar - models.ImageField(upload_to='students/', verbose_name='avatar', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'names'
        ordering = ('last_name',)
