from django import forms
# from .models import Category    # для работы с Формами, НЕ связанные с Моделями
from .models import News    # для работы с Формами, связанные с Моделями
import re
from django.core.exceptions import ValidationError

# Пример для работы с Формами, НЕ связанные с Моделями
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Контент', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_published = forms.BooleanField(label='Опубликовано?', initial=True)           # initial= - Это первоначальное значение поля
#     category = forms.ModelChoiceField(empty_label='Выберите категорию', queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={"class": "form-control"}))


# Пример для работы с Формами, связанные с Моделями
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #field = '__all__'         # Если нужно все поля из Модели добавить в форму (не рекомендуется)
        fields = ['title', 'content', 'is_published', 'category']         # Правильный вариант
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title