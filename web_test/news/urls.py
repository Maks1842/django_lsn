from django.urls import path
from .views import *

## Для теста
# urlpatterns = [
#     path('', index),
#     path('test/', test),
# ]

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
   # path('test_mkc/', name='test_mkc'),
]