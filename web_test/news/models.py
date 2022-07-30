from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')  #  verbose_name - Как поле будет отображаться в админке
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)    # blank=True  - значит поле не обязательное
    is_published = models.BooleanField(default=True, verbose_name='Успешно опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')              #Поле для связывания моделей (в данном случае для модели Category)

    def get_absolute_url(self):            #Имя метода определено Конвенцией (нельзя по другому называть), поэтому Джанго видит его по умолчанию
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']           #Если необходимо сортировать объекты ('-created_at' - в обратном порядке)


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):            #Имя метода определено Конвенцией, поэтому Джанго видит его по умолчанию
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']