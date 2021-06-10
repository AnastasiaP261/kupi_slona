from django.db import models
from kupi_slona.models import Image


class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ManyToManyField(Image)
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title
