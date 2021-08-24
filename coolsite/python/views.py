from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import python_lesson, python_section

from coolsite import settings
from django.core.mail import send_mail

from .forms import NameForm

menu = ['/python/', '/python/section/', '/python/section/5']


def index(request):
    context = {
        'title': 'Главная страница python',
        'menu': menu
    }
    return render(request, 'python/index.html', context=context)


def form_1(request):
    """Для тестирования форм отправки"""
    if request.method == 'POST': # Если данные отправлены из формы методом POST
        # Если была отправка методом POST то форма тоже создается но с привязкой
        # к данным полученным из запроса
        form = NameForm(request.POST) # Создание экземпляра класса формы
        if form.is_valid(): # Проверка данных на валидность
            # Если проверка данных методом is_valid() пройдена то все проверенные
            # данный будут доступны в атрибуте cleaned_data эти данные уже можно
            # использовать для ввода в БД
            print('='*30)
            print(form.cleaned_data)
            print('='*30)
            return HttpResponseRedirect('/python/form_1/') # Редирект при успехе
    # if request.method == 'GET':
    #     print('Отправка форм ы методом GET')
    else:
        # Если отправка была методом GET, то просто создаем экземпляр
        # формы, и отображаем пустую форму на странице.
        form = NameForm()
    context = {
        'title': 'Тест формы 1',
        'menu': menu,
        'form': form
    }
    return render(request, 'python/form_1.html', context=context)


def section(request, section):
    """Показать все уроки по выбранной теме"""
    lessons = python_lesson.objects.all()
    context = {
        'title': 'Страница разделов python',
        'menu': menu,
        'lessons': lessons
    }
    return render(request, 'python/section.html', context=context)


def lesson(request, section, lesson_id):
    """Показать конкретный урок по ID"""

    one_lesson = python_lesson.objects.get(pk=lesson_id)
    context = {
        'title': 'Страница уроков python',
        'menu': menu,
        'lesson': one_lesson
    }
    return render(request, 'python/lesson.html', context=context)

