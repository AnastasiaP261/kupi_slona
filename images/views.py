from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from images.models import Images
from .forms import ImagesForm
from django.urls import reverse_lazy
from imagekit.processors import ResizeToFit


class ImageView(DetailView):
    model = Images
    context_object_name = 'img'


class AddImage(CreateView):
    form_class = ImagesForm
    template_name = 'images/add_image.html'
    success_url = reverse_lazy('add_image')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Images.objects.all()
        return super(AddImage, self).get_context_data(**kwargs)


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
