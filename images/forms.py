from django import forms
from .models import Images


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }




# class ImagesForm(forms.Form):
#     title = forms.CharField(max_length=30, label='Название изображения:',
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     image = forms.ImageField(label="Файл:", widget=forms.FileInput(attrs={'class': 'form-control'}))
