from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()[:8]       # получение последних 8 новостей
    return render(request, 'news/index.html', {'news': news, 'active_link': 'blog'})
