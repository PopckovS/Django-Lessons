from django.db import models


class Women(models.Model):
    """Модель для таблицы о женщинах"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class Product(models.Model):
    """Модель для теста поля ImageField"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    #  корня сайта папка Изображение/
    photo = models.ImageField(upload_to="Изображения/%Y/%m/%d/")

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)



