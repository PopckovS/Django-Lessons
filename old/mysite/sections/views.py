from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Гланый метод отвечает за посадочную страницу всего раздела."""
    return render(request, 'sections/index.html')


def section(request):
    """Показать все статьи конкретного раздела."""
    print('*'*20)
    print(request)
    print(''*20)
    # return HttpResponse("Все статьи")
    return render(request, 'sections/section.html')


def article(request):
    """Показать конкретную статью по ее id БД."""
    print('*'*20)
    print(request)
    print(''*20)
    # return HttpResponse("Статья по ее ID")
    return render(request, 'sections/article.html')


