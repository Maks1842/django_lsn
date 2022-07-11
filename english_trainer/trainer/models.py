from django.db import models
from django.urls import reverse


class Words(models.Model):
    word_eng = models.CharField(max_length=150, verbose_name='Английский')
    word_transcrip = models.CharField(max_length=150, verbose_name='Транскрипция', blank=True)
    word_rus = models.CharField(max_length=150, verbose_name='Русский')
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    audio = models.FileField(upload_to='audio/%Y/%m/%d/', verbose_name='Аудио', blank=True)    # blank=True  - значит поле не обязательное
    date_eng_lessons = models.DateField(auto_now=True, verbose_name='Дата изучения английского слова')
    date_rus_lessons = models.DateField(auto_now=True, verbose_name='Дата изучения русского слова')

    # def get_absolute_url(self):            #Имя метода определено Конвенцией, поэтому Джанго видит его по умолчанию
    #     return reverse('word-add')

    def __str__(self):
        return self.word_eng

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        ordering = ['date_eng_lessons', 'date_rus_lessons']           #Если необходимо сортировать объекты ('-date_eng_lessons' - в обратном порядке)


class Statistics(models.Model):
    date_lessons = models.DateField(auto_now=True, verbose_name='Дата изучения слов')
    sum_word_eng = models.IntegerField(verbose_name='Количество изученных английских слов')
    sum_word_rus = models.IntegerField(verbose_name='Количество изученных русских слов')

    class Meta:
        verbose_name = 'Статистику'
        verbose_name_plural = 'Статистика'


class SettingsTrainer(models.Model):
    count_words = models.IntegerField(verbose_name='Изучить слов')
    min_days = models.IntegerField(verbose_name='Минимальное количество дней между тренировками')
    max_days = models.IntegerField(verbose_name='Максимальное количество дней между тренировками')

    class Meta:
        verbose_name = 'Настройки тренажера'
        verbose_name_plural = 'Настройки тренажера'