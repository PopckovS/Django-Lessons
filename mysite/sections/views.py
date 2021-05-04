from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Гланый метод отвечает за посадочную страницу всего раздела."""
    return HttpResponse("Главная")
    # return render(request, '')


