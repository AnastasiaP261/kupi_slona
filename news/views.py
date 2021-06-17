from django.shortcuts import render, get_object_or_404, redirect
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
        form = NewsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # new_obj = form.save(commit=False)
            # new_obj.user = request.user
            # new_obj.save()

            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # is_publ = form.cleaned_data['is_published']
            # author = form.cleaned_data['author']
            # photo = form.cleaned_data['photo']
            # news = News.objects.create(title=title, content=content, author=author, is_published=is_publ)
            # news.save()
            # for mem_id in list(photo):
            #     print(mem_id)
            #     news.photo.add(mem_id)
            # news.save()
            # news.photo.set(form.cleaned_data['photo'])

            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_article.html', {'form_news': form})
