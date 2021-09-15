import os
import shutil
from datetime import datetime

from PIL import Image
from django.conf import settings

"""
Модуль для стилизации изображений.
"""


def stylize_images(image, filter, alpha_value=128):
    """Главная функция обработчик"""

    # Используем секунды для создания уникальных ID
    seconds = str(datetime.today().timestamp())

    # Создаем название для временной   директории
    unique_dir = os.path.join(settings.DIR_TRANSFER, seconds)

    # Создаем директорию
    os.mkdir(unique_dir)

    # Генерирую пути для создания копий во временной папке
    new_image_jpg = os.path.join(settings.DIR_TRANSFER, seconds, os.path.basename(image))
    new_filter_jpg = os.path.join(settings.DIR_TRANSFER, seconds, os.path.basename(filter))

    # Копируем изображения в транзитную папку
    shutil.copyfile(image, new_image_jpg)
    shutil.copyfile(filter, new_filter_jpg)

    # Конвертируем файлы в png и получаем новые пути
    new_image_png = convert_jpg_to_png(new_image_jpg)
    new_filter_png = convert_jpg_to_png(new_filter_jpg)

    # Удаляем старые jpg фото
    delete_file(new_image_jpg, new_filter_jpg)

    # Добавляем фильтру прозрачность
    add_alpha_canal(new_filter_png, alpha_value)

    # Генерируем уникальное название для финального изображения на основе времени
    combine_img = os.path.join(settings.DIR_TRANSFER, seconds, f"{seconds}.png")

    # создаем финальное изображение
    create_combine_image(new_image_png, new_filter_png, combine_img)

    # Удаляем временные png фото
    delete_file(new_image_png, new_filter_png)

    # Копируем созданный стилизованный файл в общую директорию
    final_path = os.path.join(os.path.dirname(image), os.path.basename(combine_img))
    shutil.copyfile(combine_img, final_path)

    # Удаляем созданный файл
    delete_file(combine_img)

    # Удаляем временную директорию
    shutil.rmtree(unique_dir)

    # Возвращаем только название сгенерированного файла
    return os.path.basename(combine_img)

# TODO удалять по одному
def delete_file(*files):
    """Удаляем весь кортеж полученных файлов"""
    for file in files:
        os.remove(file)

# TODO переписать на регулярное выражение
def convert_jpg_to_png(photo_jpg):
    """
    Конвертирует изображение из jpg в png
    Возвращаем новый путь к картинке.
    """
    img = Image.open(photo_jpg)
    photo_png = photo_jpg.replace('.jpg', '.png')
    img.save(photo_png)
    return photo_png


def add_alpha_canal(source_png, alpha_value=128):
    """Добавляет png изображению, Альфа канал."""
    img = Image.open(source_png)
    img.putalpha(alpha_value)
    img.save(source_png)


def create_combine_image(photo_png, filter_png, result_img):
    """
    Наложение фильтра на изображение.

    Изменяет размер фильтра, подстраивая его под
    изображение, накладывает фильтр на изображение.
    """
    # Открываем изображение
    background = Image.open(photo_png)
    foreground = Image.open(filter_png)

    # Получаем размер изображения
    back_width, back_height = background.size

    # Подстраиваем размер фильтра под изображение
    foreground = foreground.resize((back_width, back_height))

    # Накладываем фильтр на фото и сохраняем
    background.paste(foreground, (0, 0), foreground)
    background.save(result_img)
