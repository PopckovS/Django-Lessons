from django.db import models

from django.db import connection

# Спец метод reverse для создания абсолютного пути URL
from django.urls import reverse


def drop_category():
    with connection.cursor() as cursor:
        cursor.execute("drop table women_category")
        cursor.fetchall()


class category(models.Model):
    """Категории для женщин"""
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Women(models.Model):
    """Модель для таблицы о женщинах"""
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     cat = self.cat  # self.value is a model field.
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Модули Django используют этот методе если он определен в модели"""
        return reverse('post', kwargs={'post_id': self.pk})
