from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView
from images.models import Images
from .forms import ImagesForm
from django.urls import reverse_lazy


class AddImage(CreateView):
    form_class = ImagesForm
    template_name = 'images/add_image.html'
    success_url = reverse_lazy('add_image')

# def add_image(request):
#     if request.method == 'POST':
#         form_img = ImagesForm(request.POST)
#         if form_img.is_valid():
#             print(form_img.cleaned_data)
#             img = Images.objects.create(**form_img.cleaned_data)
#             return HttpResponseRedirect('add_image')
#     else:
#         form_img = ImagesForm()
#     return render(request, 'images/add_image.html', {'form_img': form_img})
