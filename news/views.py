from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    # print(dir(request))
    news = News.objects.all()       # получение всех новостей
    res = '<h1>Слоновьи новости</h1>'
    for item in news:
        res += f'<div>\n<h3>{item.title}</h3>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')