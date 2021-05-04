from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sections, Articles

# Тут мы регистрируем модели, эти модели будут
# добавлены в админку, и их можно будет редактировать
admin.site.register(Sections)
admin.site.register(Articles)
