from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='blog'),
    path('article/<int:article_id>/', get_article, name='article'),
    path('article/add_article/', add_article, name='add_article'),
]
