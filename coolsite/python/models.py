from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class python_section(models.Model):
    """Разделы уроков по python"""
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")


class python_lesson(models.Model):
    """Уроки по разделам дял python"""
    python_section = models.ForeignKey(python_section, on_delete=models.CASCADE, verbose_name="Родительский раздел")
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    # Поле заменено на специальный тип для html редактора-Ckeditor
    content = RichTextUploadingField(config_name='default', blank=True, verbose_name="Текст")
    # content = models.TextField(blank=True, verbose_name="Текст")

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

