from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Модель для разделов
class Sections(models.Model):
    title = models.CharField(max_length=250)
    text = RichTextUploadingField()


# Модель для Статей
class Articles(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    # votes = models.IntegerField(default=0)
    text = RichTextUploadingField()
    pub_date = models.DateTimeField('date published')
