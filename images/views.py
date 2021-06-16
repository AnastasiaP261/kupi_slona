from django.shortcuts import render
from .forms import ImagesForm


def add_image(request):
    if request.method == 'POST':
        pass
    else:
        form_img = ImagesForm()
    return render(request, 'images/add_image.html', {'form_img': form_img})
