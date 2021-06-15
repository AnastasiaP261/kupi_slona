from django.contrib import admin
from images.models import Images
from PIL import Image as PImage
from kupi_slona.settings import STATIC_URL, MEDIA_URL
import os


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        img = PImage.open(obj.image)
        max_size = (1300, 750)
        empty_list = PImage.new('RGB', max_size, 'white')

        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size)
        empty_list.paste(img, ((max_size[0] - img.size[0]) // 2, (max_size[1] - img.size[1]) // 2))

        path = os.path.join(STATIC_URL, MEDIA_URL, obj.image.name)
        empty_list.save(fp=path, format=img.format)
        new_im = Images(title=obj.title, image=obj.image.name)

        return super().save_model(request, new_im, form, change)


admin.site.register(Images, ImagesAdmin)
