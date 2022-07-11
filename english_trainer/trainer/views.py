from django.shortcuts import render, get_object_or_404

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
        pass
    else:
        form = WordsForm()
    return render(request, 'trainer/word_add.html', {'form': form, 'title': 'English trainer'})

def lesson_en(request):
    context = {
        'title': 'English trainer',
    }
    return render(request, 'trainer/lesson_en.html', context)

def lesson_rus(request):
    context = {
        'title': 'English trainer',
    }
    return render(request, 'trainer/lesson_rus.html', context)

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

# def add_words(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = WordsForm()
#     return render(request, 'trainer/word_add.html', {'form': form})
