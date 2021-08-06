from django.urls import path, re_path

# Импорт видов от приложения women
from women.views import *

# URL внутри приложения women
urlpatterns = [
    path('', index),

    # path('categories', categories),
    path('categories/<int:catID>', categories),
    # path('categories/<slug:cat>', categories),

    # Использование спец функции re_path() для работы рег.выр в URL
    # URL сработает если будет только 4 цифры
    re_path(r'^archive/(?P<year>[0-9]{4})', archive),
]


