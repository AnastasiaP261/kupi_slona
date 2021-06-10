from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.order_by('-created_at')       # получение всех новостей
    return render(request, 'news/index.html', {'news': news})
