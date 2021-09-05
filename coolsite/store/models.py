from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    # cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)

    # , related_name = 'snippets'
    # owner = models.ForeignKey('auth.User', default=True, blank=True, on_delete=models.CASCADE)

    owner = models.ForeignKey(User, default=True, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/store/", blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return f'Id {self.id}:  {self.name}'


