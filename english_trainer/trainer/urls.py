from django.urls import path
from .views import *


#V1 Основной вариант
urlpatterns = [
    path('', index, name='home'),
]