from django.apps import AppConfig


# Настройки проекта women
class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    # Название приложения
    name = 'women'

    # Имя которое будет отображаться в админ панели
    # для всего этого приложения
    verbose_name = 'Женщины мира'

