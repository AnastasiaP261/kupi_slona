from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()[:10]       # получение всех новостей
    val = [True, False]
    indexes = list([val[i % 2] for i in range(len(news))])
    return render(request, 'news/blog.html', {'content': zip(news, indexes)})
