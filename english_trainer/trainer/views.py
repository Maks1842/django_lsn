from django.shortcuts import render, get_object_or_404, redirect

from .models import Words
from .forms import WordsForm


# Боевой Контент главной страницы
def index(request):
    words = Words.objects.all()   #Если необходимо сортировать объекты ('-created_at' - в обратном порядке)
    context = {
        'words': words,
        'title': 'English trainer',
    }
    return render(request, 'trainer/index.html', context)

def word_add(request):
    if request.method == 'POST':
        form = WordsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
        if form.is_valid():                                  # Проверяю прошла ли Форма валидацию
            form.save()                               # Данной строкой введенные данные в Форме, сохраняются в БД
            return redirect('word-add')
    else:
        form = WordsForm()
    return render(request, 'trainer/word_add.html', {'form': form, 'title': 'English trainer'})

def lesson_en(request):
    if request.method == 'POST':
        form = WordsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
    else:
        form = WordsForm()
    return render(request, 'trainer/lesson_en.html', {'form': form, 'title': 'English trainer'})

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
