# Generated by Django 4.0.5 on 2022-06-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_words', models.IntegerField(verbose_name='Изучить слов')),
                ('min_days', models.IntegerField(verbose_name='Минимальное количество дней между тренировками')),
                ('max_days', models.IntegerField(verbose_name='Максимальное количество дней между тренировками')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_lessons', models.DateField(auto_now=True, verbose_name='Дата изучения слов')),
                ('sum_word_eng', models.IntegerField(verbose_name='Количество изученных английских слов')),
                ('sum_word_rus', models.IntegerField(verbose_name='Количество изученных русских слов')),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_eng', models.CharField(max_length=150, verbose_name='Английский')),
                ('word_transcrip', models.CharField(blank=True, max_length=150, verbose_name='Транскрипция')),
                ('word_rus', models.CharField(max_length=150, verbose_name='Русский')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('audio', models.FileField(blank=True, upload_to='audio/%Y/%m/%d/', verbose_name='Аудио')),
                ('date_eng_lessons', models.DateField(auto_now=True, verbose_name='Дата изучения английского слова')),
                ('date_rus_lessons', models.DateField(auto_now=True, verbose_name='Дата изучения русского слова')),
            ],
        ),
    ]