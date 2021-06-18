from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='blog'),
    path('', HomeNews.as_view(), name='blog'),
    # path('article/<int:article_id>/', get_article, name='article'),
    path('article/<int:pk>/', ViewNews.as_view(), name='article'),
    # path('article/add_article/', add_article, name='add_article'),
    path('article/add_article/', CreateArticle.as_view(), name='add_article'),
]
