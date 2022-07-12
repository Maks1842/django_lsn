from django import forms

class WordsForm(forms.Form):
    word_eng = forms.CharField(max_length=150, label='Английский')
    word_transcrip = forms.CharField(max_length=150, label='Транскрипция', required=False)
    word_rus = forms.CharField(max_length=150, label='Русский')
    comment = forms.CharField(label='Комментарий', required=False)