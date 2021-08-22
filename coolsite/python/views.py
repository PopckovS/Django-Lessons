from django.http import HttpResponse
from django.shortcuts import render

from .models import python_lesson, python_section

from coolsite import settings
from django.core.mail import send_mail

menu = ['/python/', '/python/section/', '/python/section/5']


def index(request):
    context = {
        'title': 'Главная страница python',
        'menu': menu
    }
    return render(request, 'python/index.html', context=context)


def section(request, section):
    """Показать все уроки по выбранной теме"""
    lessons = python_lesson.objects.all()
    context = {
        'title': 'Страница разделов python',
        'menu': menu,
        'lessons': lessons
    }
    send_mail(
        'Hello World !',
        'body of message',
        settings.EMAIL_HOST_USER,
        ['popckovM5@yandex.ru'],
        fail_silently=False,
    )
    return render(request, 'python/section.html', context=context)


def lesson(request, section, lesson_id):
    """Показать конкретный урок по ID"""
    lessons = python_lesson.objects.all()
    context = {
        'title': 'Страница уроков python',
        'menu': menu
    }
    return render(request, 'python/lesson.html', context=context)

