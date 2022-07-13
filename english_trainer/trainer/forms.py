from django import forms
from .models import Words

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
