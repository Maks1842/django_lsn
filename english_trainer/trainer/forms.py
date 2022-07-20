from django import forms
from .models import Words

# Форма связанная с моделью
class WordsForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = ['word_eng', 'word_transcrip', 'word_rus', 'comment']
        widgets = {
            'word_eng': forms.TextInput(attrs={"class": "form-control"}),
            'word_transcrip': forms.TextInput(attrs={"class": "form-control"}),
            'word_rus': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


# Форма НЕ связанная с моделью
class WordAnswer(forms.Form):
    content = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "name": "word-answer", "style": "font-size: 32px", "id": "text_word"}))
