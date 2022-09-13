from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, pk):
    return HttpResponse(f'Пост на тему: {pk}')