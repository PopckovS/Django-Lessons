from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *
# from .models import Women
# from .models import category
# from .models import drop_category, create_category

menu = [
        {'title': 'О сайте',         'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь',  'url_name': 'contact'},
        {'title': 'Войти',           'url_name': 'login'},
    ]


def index(request):
    """Главная страница"""
    posts = Women.objects.all()
    all_category = category.objects.all()
    context = {
        'title': 'Главная страница Women',
        'posts': posts,
        'menu': menu,
        'all_category': all_category,
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=context)


def show_category(request, cat_id):
    """Показать все записи из конкретной категории"""
    try:
        category.objects.get(pk=cat_id)
    except:
        raise Http404('Такой категории не найдено !')

    posts = Women.objects.filter(cat_id=cat_id)
    all_category = category.objects.all()
    context = {
        'title': 'Статьи по категориям',
        'menu': menu,
        'all_category': all_category,
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    """О приложении"""
    context = {
        'title': 'Women о сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=context)


def contact(request):
    """Контакты"""
    return HttpResponse('contact')


def login(request):
    """Логин"""
    return HttpResponse('login')


def add_page(request):
    return HttpResponse('add_page')


def show_post(request, post_id):
    return HttpResponse(f'show_post post_id = {post_id}')


def pageNotFound(request, exception):
    """Отображение страницы ошибок"""
    return HttpResponseNotFound("<h1>Страница не найдена, ошибка 404</h1>")

