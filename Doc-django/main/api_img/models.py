from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from PIL import Image
import os

from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver, Signal


def validate_file_image_max_size(image):
    """Валидатор, для проверки размера изображение, не более 2 MB"""
    if image.size > settings.FILE_MAX_SIZE:
        raise ValidationError('Файл слишком большой, размер должен быть не больше 2 MB')


class ImageType(models.TextChoices):
    """
    Класс для описания типов изображений,
    которые можно вносить в БД.
    """
    PHOTO = ('photo', 'photo')
    FILTER = ('filter', 'filter')
    RESULT = ('result', 'result')


class Images(models.Model):
    """Модель для CRUD операций с изображениями"""

    # Сообщение ошибки, для недопустимых форматов загружаемых изображений
    big_image_message_error = ', '.join(settings.UPLOAD_IMAGE)

    type = models.CharField(
        max_length=6,
        choices=ImageType.choices,
        default=ImageType.PHOTO,
        verbose_name='Тип изображения'
    )
    big_image = models.ImageField(
        upload_to=settings.BIG_IMG_PATH,
        blank=True,
        null=True,
        validators=[
          FileExtensionValidator(
              allowed_extensions=settings.UPLOAD_IMAGE,
              message=f'Файл должен быть одним из: {big_image_message_error}'
          ),
          validate_file_image_max_size,
        ],
        verbose_name='Большое изображение',
        )
    min_image = models.ImageField(
        upload_to=settings.SMALL_IMG_PATH,
        blank=True,
        null=True,
        verbose_name='Маленькое изображение'
    )
    # parent_photo = models.ForeignKey('Images', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Фото родитель')
    # parent_filter = models.ForeignKey('Images', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Фильтр родитель')

    def __str__(self):
        return f'Id {self.id}:  {self.type}'

    def get_path_to_small_photo(self):
        """Путь к директории мини версии картинки"""
        return "{0}/{1}".format(settings.MEDIA_ROOT, settings.SMALL_IMG_PATH)


def create_small_img(instance, size=500):
    """Создание мини версии изображения"""
    img = Image.open(instance.big_image.path)
    if img.height > size or img.width > size:
        img.thumbnail((size, size))
        img.save(instance.get_path_to_small_photo() + os.path.basename(instance.big_image.path))
        min_image_path = "{0}{1}".format(settings.SMALL_IMG_PATH, os.path.basename(instance.big_image.path))
    else:
        min_image_path = instance.big_image
    Images.objects.filter(pk=instance.pk).update(min_image=min_image_path)


@receiver(pre_save, sender=Images)
def on_change_pre(sender, instance, **kwargs):
    """Сигнал pre_save - Если обновляются изображения, то удаляем старые."""
    if instance.id is not None:
        previous = Images.objects.get(id=instance.id)
        if previous.big_image != instance.big_image and os.path.isfile(previous.big_image.path):
            os.remove(previous.big_image.path)
        if previous.min_image != instance.min_image and os.path.isfile(previous.min_image.path):
            os.remove(previous.min_image.path)


@receiver(post_save, sender=Images)
def on_change_post(sender, instance, **kwargs):
    """Сигнал post_save - Создаем мини изображение."""
    if instance.big_image and os.path.isfile(instance.big_image.path):
        create_small_img(instance, size=500)


@receiver(pre_delete, sender=Images)
def on_delete_pre(sender, instance, **kwargs):
    """Сигнал pre_delete - Удаляем изображения привязанные к записи в модели."""
    if instance.big_image and os.path.isfile(instance.big_image.path):
        os.remove(instance.big_image.path)
    if instance.min_image and os.path.isfile(instance.min_image.path):
        os.remove(instance.min_image.path)
