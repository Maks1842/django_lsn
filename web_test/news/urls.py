from django.urls import path
from .views import *

## Для теста
# urlpatterns = [
#     path('', index),
#     path('test/', test),
# ]

#V1 Основной вариант
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add-news/', add_news, name='add-news'),
]