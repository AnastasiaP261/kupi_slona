from django import forms
from images.models import Images


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100,
                            label='Название:',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст статьи:',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    photo = forms.ModelMultipleChoiceField(queryset=Images.objects.all(),
                                           label='Прикрепить уже загруженные изображения:',
                                           widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    is_published = forms.BooleanField(initial=True,
                                      label='Опубликовано:')
    author = forms.CharField(max_length=30,
                             label='Автор:',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
