from django.urls import path
from .views import *

urlpatterns = [
    # path('add_image/', add_image, name='add_image'),
    path('add_image/', AddImage.as_view(), name='add_image'),
]
