from django import template
from women.models import *

# Создаем экземпляр для регистрации шаблонных тегов
register = template.Library()

# Далее создаем функции для работы простого тега


# Название функции для тега можно давать произвольно
# Для регистрации данной функции как тега используется
# специальный декоратор
@register.simple_tag()
def get_categories():
    """Возвращает все категории"""
    return category.objects.all()



