from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.db import models


class Images(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    type = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип')
    big_image = models.ImageField(upload_to=settings.SMALL_IMG_PATH,
                                  null=True, blank=True,
                                  verbose_name='Маленькое изображение')

    def __str__(self):
        return f'Id {self.id}:  {self.type}'
