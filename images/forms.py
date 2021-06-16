from django import forms


class ImagesForm(forms.Form):
    title = forms.CharField(max_length=30, label='Название изображения:',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label="Файл:", widget=forms.FileInput(attrs={'class': 'form-control'}))
