from celery import shared_task

from django.conf import settings
from image_transform.img_stylize import stylize_images
from .models import Images
from image_transform.neural_stylize import neural_style_transfer


@shared_task
def img_style(photo_image_path, filter_image_path, img_id):
    """Таск создает новое изображение, и обновляет поле записи в БД"""

    # Выбираем функцию стилизации изображения
    stylize_img = neural_style_transfer(img_photo=photo_image_path, img_style=filter_image_path, quality=settings.QUALITY)
    # stylize_img = stylize_images(image=photo_image_path, filter=filter_image_path, alpha_value=settings.ALPHA_VALUE)

    # Обновляем путь к созданному изображению
    img = Images.objects.get(pk=img_id)
    img.big_image = settings.BIG_IMG_PATH + stylize_img
    img.save()
