from django.shortcuts import render, get_object_or_404
from .models import News
from .forms import NewsForm
from images.forms import ImagesForm


def index(request):
    news = News.objects.all()[:8]       # получение последних 8 новостей
    return render(request, 'news/index.html', {'news': news, 'active_link': 'blog'})


def get_article(request, article_id):
    # news_item = News.objects.get(pk=article_id)
    news_item = get_object_or_404(News, pk=article_id)
    return render(request, 'news/view_article.html', {'news_item': news_item})


def add_article(request):
    if request.method == 'POST':
        pass
    else:
        form_news = NewsForm()
    return render(request, 'news/add_article.html', {'form_news': form_news})
