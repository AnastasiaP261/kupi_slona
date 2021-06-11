from django.contrib import admin
from images.models import Images


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Images, ImagesAdmin)