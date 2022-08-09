from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .utils import MyMixin
from django.contrib import messages
from django.contrib.auth import login, logout


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


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # if form.is_valid():                    ## V1 - после регистарции перенаправляем на страницу авторизации
        #     form.save()
        #     messages.success(request, 'Вы успешно зарегистрировались')   # Сообщение для пользователя из формы
        #     return redirect('login')                      ## V1 - После успешной регистрации перенаправить на страницу Авторизации

        if form.is_valid():                    ## V2 - после регистрации сразу авторизуем
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')           # После успешной авторизации можно перенаправить куда-нибудь пользователя (например на главную страницу)

        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


# Авторизация пользователя
def user_login(request):
    if request.method == 'POST':                            # Если данные к нам пришли методом 'POST'
        form = UserLoginForm(data=request.POST)             # Тогда создаем экземпляр формы и связываем его с данными (обязательно указать data=)
        if form.is_valid():                                 # Проверяем, если форма валидна
            user = form.get_user()                          # то можно авторизовать пользователя. Для этого его нужно получить с помощью .get_user()
            login(request, user)                            # далее в метод login передаю объект Юзера
            return redirect('home')                         # После успешной авторизации можно перенаправить куда-нибудь пользователя (например на главную страницу)
    else:
        form = UserLoginForm()                              # Если данные пришли не методом 'POST', то просто создать объект формы не связанный с данными

    return render(request, 'news/login.html', {'form': form})     # и далее в шаблон html передаем форму , {'form': form}


# Выход пользователя из учетки
def user_logout(request):
    logout(request)
    return redirect('login')


# Пример работы с контоллерами классов
class HomeNews(MyMixin, ListView):           # Данный класс заменяет контроллер функции >>> def index(request):
    model = News                    # Указываю из какой Модели буду получать данныу
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}
    # queryset = News.objects.select_related('category')          # Данный атрибут указывается здесь, если отсутствует метод def get_queryset(self):. Если этот метод есть в классе, то атрибут указывать там
    mixin_prop = 'hello world'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')     # .select_related('category') - данный метод реализаует Жадный запрос. Если без него - то будет Ленивый запрос


class NewsByCategory(ListView):       # Данный класс заменяет контроллер функции >>> def get_category(request, category_id):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False               # Специальный атрибут класса. Запрещает показ пустых списков. По умолчанию имеет значение True


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')     # .select_related('category') - данный метод реализаует Жадный запрос. Если без него - то будет Ленивый запрос


class ViewNews(DetailView):         # Данный класс заменяет контроллер функции >>> def view_news(request, news_id):
    model = News                    # Указываю из какой Модели буду получать данные
    context_object_name = 'news_item'
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'


# Пример для работы с Формами, связанные с Моделями
class CreateNews(LoginRequiredMixin, CreateView):         # Данный класс заменяет контроллер функции >>> def add_news(request):
    form_class = NewsForm                   # Связываю форму с существующей моделью
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')      # После сохранения данных, перенаправляет пользователя по указанному адресу. По умолчанию (без данного метода) редирект происходит на текущую страницу
    login_url = '/admin/'                 # Вариант 1 - перенаправляет на Админку
    # login_url = reverse_lazy('home')        # Вариант 2 - перенаправляет на указанную страницу
    # raise_exception = True                  # Вариант 3 - перенаправляет на страницу "ошибка 403" доступ запрещен


# Пример работы с контоллерами функций
# Боевой Контент главной страницы
# def index(request):
#     news = News.objects.all()   #Если необходимо отображать объекты в порядке как в ДБ
#     # news = News.objects.order_by('-created_at')   #Если необходимо сортировать объекты ('-created_at' - в обратном порядке)
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})

# def view_news(request, news_id):
#     #news_item = News.objects.get(pk=news_id)                           #V1
#     news_item = get_object_or_404(News, pk=news_id)                     #V2 с обработчиком ошибки некорректного адреса страницы
#     return render(request, 'news/view_news.html', {"news_item": news_item})

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
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)                        # Данная строка создает Форму связанную с данными Модели
#         if form.is_valid():                                  # Проверяю прошла ли Форма валидацию
#             print(form.cleaned_data)
#             # news = form.save()                               # Данной строкой введенные данные в Форме, сохраняются в БД
#             # return redirect(news)                            # После сохранения данных, перенаправляет пользователя по указанному адресу (можно на сам созданный объект или на какую-либо страничку)
#     else:
#         form = NewsForm()                                    # Данная строка создает пустую Форму не связанную с данными Модели
#     return render(request, 'news/add_news.html', {'form': form})