from django.urls import path, re_path
from . import views

urlpatterns = [
    # URL: /python/ Домашняя страница
    path('', views.index, name='home'),

    # URL: /python/section/ показать все уроки по данной теме
    path('<str:section>/', views.section, name='section'),

    # URL: /python/section/5/ показать урок конкретной темы по его id
    path('<str:section>/<int:lesson_id>/', views.lesson, name='lesson'),
]
