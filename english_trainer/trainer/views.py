from django.shortcuts import render, get_object_or_404

from .models import Words

# Боевой Контент главной страницы
def index(request):
    words = Words.objects.all()   #Если необходимо сортировать объекты ('-created_at' - в обратном порядке)
    context = {
        'words': words,
        'title': 'English trainer',
    }
    return render(request, 'trainer/index.html', context)

def word_add(request):
    context = {
        'title': 'English trainer',
    }
    return render(request, 'trainer/word_add.html', context)