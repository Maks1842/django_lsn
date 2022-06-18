from django.contrib import admin
from .models import News, Category


# Настройка админки
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')      # Указываю какие поля отображать
    list_display_links = ('id', 'title')                                            # Указываю какие поля работают как ссылки
    search_fields = ('title', 'content')                                            # Указываю по каким полям можно осуществлять поиск
    list_editable = ('is_published',)                                             # Возможность редактирования поля
    list_filter = ('is_published', 'category')                                   # Возможность фильтровать поля

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)             # В кортеже из одного элемента обязательно наличие запятой в конце


admin.site.register(News, NewsAdmin)            #!!!Важно соблюдать последовательность регистрации модэлей
admin.site.register(Category, CategoryAdmin)
