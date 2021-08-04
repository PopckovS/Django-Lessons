from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Представление для обработки главной страницы.

    request - ссылка на класс HttpRequest с инфой о запросе, сессии,
     куки,, заголовки и тд..

    return - на выходе должен быть экземпляр класса HttpResponse
    """
    return HttpResponse("Привет мир !")



