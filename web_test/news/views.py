from django.shortcuts import render
from django.http import HttpResponse

from .models import News


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


## Боевой Контент главной страницы
def index(request):
    # news = News.objects.all()   #Если необходимо отображать объекты в порядке как в ДБ
    news = News.objects.order_by('-created_at')   #Если необходимо сортировать объекты ('-created_at' - в обратном порядке)
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)


