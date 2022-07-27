from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
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


# Пример работы с контоллерами классов
class HomeNews(ListView):           # Данный класс заменыет контроллер функции def index(request):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# Пример работы с контоллерами функций
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

# Пример для работы с Формами, НЕ связанные с Моделями
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
#         if form.is_valid():                                  # Проверяю прошла ли Форма валидацию
#             news = News.objects.create(**form.cleaned_data)  # Данной строкой введенные данные в Форме, сохраняются в БД
#             return redirect(news)                            # После сохранения данных, перенаправляет пользователя по указанному адресу (можно на сам созданный объект или на какую-либо страничку)
#     else:
#         form = NewsForm()                                    # Данная строка создает пустую Форму не связанную с данными Модели
#     return render(request, 'news/add_news.html', {'form': form})


# Пример для работы с Формами, связанные с Моделями
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
        if form.is_valid():                                  # Проверяю прошла ли Форма валидацию
            print(form.cleaned_data)
            # news = form.save()                               # Данной строкой введенные данные в Форме, сохраняются в БД
            # return redirect(news)                            # После сохранения данных, перенаправляет пользователя по указанному адресу (можно на сам созданный объект или на какую-либо страничку)
    else:
        form = NewsForm()                                    # Данная строка создает пустую Форму не связанную с данными Модели
    return render(request, 'news/add_news.html', {'form': form})