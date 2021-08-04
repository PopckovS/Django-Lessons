from django.urls import path

# Импорт видов от приложения women
from women.views import index, categories

# URL внутри приложения women
urlpatterns = [
    path('', index),
    path('categories', categories),
]


