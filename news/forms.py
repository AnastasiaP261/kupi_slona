from django import forms
from images.models import Images
from .models import News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'photo', 'content', 'is_published', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '6'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 12}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # title = forms.CharField(max_length=100,
    #                         label='Название:',
    #                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Текст статьи:',
    #                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    # # photo = forms.ModelMultipleChoiceField(queryset=Images.objects.all(),
    # #                                        label='Прикрепить уже загруженные изображения:',
    # #                                        required=False,
    # #                                        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    # is_published = forms.BooleanField(initial=True,
    #                                   label='Опубликовано:')
    # author = forms.CharField(max_length=30,
    #                          label='Автор:',
    #                          widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_title(self):
        title = self.cleaned_data['title']
        if not re.match(r'''^[a-zA-Zа-яА-Я 0-9,.\-"!?']+$''', title):
            raise ValidationError('''В названии могут присутствовать только латиница,
            кириллица, цифры, символы пунктуации и знак пробела.''')
        return title





