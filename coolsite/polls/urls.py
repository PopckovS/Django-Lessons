from django.urls import path, re_path
from . import views

urlpatterns = [
    # URL: /polls/ Домашняя страница
    path('', views.index, name='home'),

    # URL: /polls/<id:int>/ Показать вопрос по ID
    path('<int:question_id>', views.detail, name='detail'),

    # URL: /polls/<id:int>/results/ Показать результат опроса по ID
    path('<int:question_id>/results/', views.results, name='results'),

    # URL: /polls/<id:int>/vote/ Проголосовать по ID
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
