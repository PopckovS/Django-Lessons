import os
from datetime import datetime
from io import BytesIO

from celery import shared_task
import random
import string
from .models import Images

from image_transform.neural_stylize import neural_style_transfer

from django.core.files.base import ContentFile
from django.core.files import File
from django.core.files.images import ImageFile

@shared_task
def create_new_object():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_img = Images.objects.create(name=random_name, type='картинка')
    return new_img


@shared_task
def img_style(photo_image_path, filter_image_path):
    stylize_img = neural_style_transfer(
        img_photo=photo_image_path,
        img_style=filter_image_path,
        quality=5
    )


    # new_img = Images.objects.create(name='НОВОЕ ИЗОБРАЖЕНИЕ-999', type='НОВЫЙ ТИП-999', image=stylize_img)

    new_img = Images()
    new_img.name = 'НОВОЕ ИЗОБРАЖЕНИЕ-999'
    new_img.type = stylize_img
    new_img.big_image = stylize_img

    new_img.save()

    # r = File.open(stylize_img)
    #
    # new_img.big_image.save('stylize_img.png', r)
    # new_img.big_image.save('stylize_img', ContentFile(stylize_img))
    # new_img.big_image.save(os.path.basename(stylize_img), ContentFile(data))

    # new_img.save()

    return stylize_img


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)





