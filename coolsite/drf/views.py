from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {}
    return HttpResponse('DRF index')
    # return render(request, 'women/index.html', context=context)


def show_post(request, post_id):
    return HttpResponse(f'show_post post_id = {post_id}')

