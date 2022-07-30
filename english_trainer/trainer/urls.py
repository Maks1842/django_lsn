from django.urls import path
from .views import *


#V1 Основной вариант
urlpatterns = [
    path('', index, name='home'),
    path('word-add/', word_add, name='word-add'),
    path('lesson-en/', lesson_en, name='lesson-en'),
    path('lesson-rus/', lesson_rus, name='lesson-rus'),
    path('customization/', customization, name='customization'),
    path('statistics/', statistics, name='statistics'),
    path('lesson-en/word-answer/', word_answer, name='word-answer'),
    path('lesson-en/word-help/', word_help, name='word-help'),
    path('lesson-rus/word-answer/', word_answer_rus, name='word-answer-rus'),
    path('lesson-rus/word-help/', word_help_rus, name='word-help-rus'),
]