# Импортируем модуль для регистрации моделей в админке
from django.contrib import admin

# Импортируем модель для регистрации
from .models import Question, Choice

# регистрируем модель в админке как поставщика данных
admin.site.register(Choice)
admin.site.register(Question)
