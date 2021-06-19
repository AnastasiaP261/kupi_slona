from django.db import models
from django.utils.html import format_html
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.urls import reverse_lazy


class Images(models.Model):
    title = models.CharField(max_length=30, verbose_name='Имя')
    # image = models.ImageField(verbose_name="Расположение")
    image = ProcessedImageField(processors=[ResizeToFit(
                                                            width=1300,
                                                            height=750,
                                                            mat_color='white',
                                                            upscale=False,
                                                        )],
                                verbose_name="Расположение")

    def __str__(self):
        return self.title

    # def get_thumbnail(self):
    #     img = self.image
    #
    #     return format_html('<img src="/images/{}" class="img-thumbnail" alt="...">', img,)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"
        ordering = ['title', 'id']

    def get_absolute_url(self):
        return reverse_lazy('view_image', kwargs={'pk': self.pk})

