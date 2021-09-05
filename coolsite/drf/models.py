from django.db import models


class Post(models.Model):
    """Модель для работы с статьями"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title
