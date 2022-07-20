from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Words
from .forms import WordsForm, WordAnswer
from .config import FileStorage
import random


# Извлечение всех данных из БД. Контент главной страницы
def index(request):
    # words = Words.objects.all()                 #Выбрать все объекты по порядку
    words = Words.objects.order_by('-pk')   #Если необходимо сортировать объекты ('-id' - в обратном порядке)
    context = {
        'words': words,
        'title': 'English trainer',
    }
    return render(request, 'trainer/index.html', context)

# Добавление данных в БД
def word_add(request):
    if request.method == 'POST':
        form = WordsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
        if form.is_valid():                                  # Проверяю прошла ли Форма валидацию
            form.save()                               # Данной строкой введенные данные в Форме, сохраняются в БД
            return redirect('home')
    else:
        form = WordsForm()
    return render(request, 'trainer/word_add.html', {'form': form, 'title': 'English trainer'})



def lesson_rus(request):
    if request.method == 'POST':
        form = WordsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
    else:
        form = WordsForm()
    return render(request, 'trainer/lesson_rus.html', {'form': form, 'title': 'English trainer'})

def customization(request):
    context = {
        'title': 'English trainer',
    }
    return render(request, 'trainer/customization.html', context)

def statistics(request):
    context = {
        'title': 'English trainer',
    }
    return render(request, 'trainer/statistics.html', context)


def lesson_en(request):
    word = Words.objects.values('id', 'word_eng', 'word_transcrip', 'comment').order_by('?').first()
    word_id = word['id']
    word_en = word['word_eng']
    word_tr = word['word_transcrip']
    word_com = word['comment']
    FileStorage.word_id = word_id

    form = WordAnswer(request.GET)                        # Данная строка создает Форму связанную с данными Модели

    # if request.method == 'GET':
    #     form = WordAnswer(request.GET)                        # Данная строка создает Форму связанную с данными Модели
    #     if form.is_valid():
    #         print(f'Что же получилось? {form.cleaned_data}')
    # else:
    #     form = WordAnswer()

    context = {
        'word_en': word_en,
        'word_tr': word_tr,
        'word_com': word_com,
        'title': 'English trainer',
        'form': form,
    }
    return render(request, 'trainer/lesson_en.html', context)


def word_answer(request):
    word_id = FileStorage.word_id
    if request.method == 'GET':
        word_answer = request.GET["word-answer"]
        word = Words.objects.values('word_rus').get(pk=word_id)
        word_rus = word['word_rus']

        if word_answer == word_rus:
            print(f'{word_answer} = {word_rus} ИСТИНА')
            return HttpResponse('ok', content_type='text/html')
        else:
            print(f'{word_answer} = {word_rus} ЛОЖЬ')
            return HttpResponse('no', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')
        # context = {
        #     'word_rus': word_rus,
        # }
    # return render(request, 'trainer/lesson_en.html', context)


def word_input_answer(request):
    pass