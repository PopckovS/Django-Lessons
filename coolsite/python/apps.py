from django.apps import AppConfig


class PythonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'python'

    # Установить специальное название для приложения в админке
    verbose_name = "Уроки по Python"

