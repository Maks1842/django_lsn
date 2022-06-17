from django.urls import path
from .views import *

## Для теста
# urlpatterns = [
#     path('', index),
#     path('test/', test),
# ]

urlpatterns = [
    path('', index),
]