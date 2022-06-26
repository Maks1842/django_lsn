from django.contrib import admin
from .models import Words, Statistics, SettingsTrainer


# Настройка админки
class WordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'word_eng', 'word_transcrip', 'word_rus', 'comment', 'date_eng_lessons', 'date_rus_lessons')      # Указываю какие поля отображать
    search_fields = ('word_eng', 'word_rus')                                            # Указываю по каким полям можно осуществлять поиск
    list_editable = ('word_eng', 'word_transcrip', 'word_rus', 'comment')                                                   # Возможность редактирования поля
    list_filter = ('word_eng', 'word_rus', 'date_eng_lessons', 'date_rus_lessons')                                          # Возможность фильтровать поля


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_lessons', 'sum_word_eng', 'sum_word_rus')


class SettingsTrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'count_words', 'min_days', 'max_days')


admin.site.register(Words, WordsAdmin)            #!!!Важно соблюдать последовательность регистрации модэлей
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(SettingsTrainer, SettingsTrainerAdmin)
