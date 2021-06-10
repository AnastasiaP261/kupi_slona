from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images/news/%Y/%m/')
