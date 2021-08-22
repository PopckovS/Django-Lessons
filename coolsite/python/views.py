from django.http import HttpResponse
from django.shortcuts import render

menu = ['/python/', '/python/section/', '/python/section/5']


def index(request):
    context = {
        'title': 'Главная страница python',
        'menu': menu
    }
    return render(request, 'python/index.html', context=context)


def section(request, section):
    context = {
        'title': 'Страница разделов python',
        'menu': menu
    }
    return render(request, 'python/section.html', context=context)


def lesson(request, section, lesson_id):
    context = {
        'title': 'Страница уроков python',
        'menu': menu
    }
    return render(request, 'python/lesson.html', context=context)

