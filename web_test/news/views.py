from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse

from .models import News, Category
from .forms import NewsForm


# def index(request):
#     # print(dir(request))
#     return HttpResponse('Hello world')

## Тестовый Контент главной страницы
# def index(request):
#     news = News.objects.all()
#     print(news)
#     res = '<h1>Список новостей</h1>'           ## Создаю заголовок первого уровня
#     for item in news:
#         res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
#     return HttpResponse(res)

# def test(request):
#     return HttpResponse('<h1>Тестовая страница</h1>')


# Боевой Контент главной страницы
def index(request):
    news = News.objects.all()   #Если необходимо отображать объекты в порядке как в ДБ
    # news = News.objects.order_by('-created_at')   #Если необходимо сортировать объекты ('-created_at' - в обратном порядке)
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)                           #V1
    news_item = get_object_or_404(News, pk=news_id)                     #V2 с обработчиком ошибки некорректного адреса страницы
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)                        #Данная строка связывает Форму с данными
        if form.is_valid():                                  # Проверяю прошла ли Форма валидацию
            news = News.objects.create(**form.cleaned_data)         # Данной строкой введенные данные в Форме, сохраняются в БД
            return redirect(news)                            # После сохранения данных, перенаправляет пользователя по указанному адресу (можно на сам созданный объект или на какую-либо страничку)
    else:
        form = NewsForm()                                             #Данная строка не связывает Форму с данными
    return render(request, 'news/add_news.html', {'form': form})
