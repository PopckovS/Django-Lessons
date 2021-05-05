from django.urls import path, include
from . import views

# Внутрении пути раздела, сопоставляют URL адреса
# методам что на них будут отвечать.
urlpatterns = [
    path('', views.index, name='index'),
    path('section/', views.section, name='section'),
    path('article/', views.article, name='articles'),
    # path('<str:section>/<int:article>', views.article, name='article'),
]
