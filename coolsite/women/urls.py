from django.urls import path, re_path

# Импорт видов от приложения women
from women.views import *

# URL внутри приложения women
urlpatterns = [
    path('', index, name='home'),

    path('categories/<int:catID>', categories, name='categories'),

    path('about/', about, name='about'),

    re_path(r'^archive/(?P<year>[0-9]{4})', archive, name='archive'),
]

