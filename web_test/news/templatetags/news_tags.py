'''Модуль для создания своих тэгов'''


from django import template
from  news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()

# #V1
# @register.inclusion_tag('news/list_categories.html')
# def show_categories():
#     categories = Category.objects.all()
#     return {"categories": categories}

#V2 Возможность передовать аргументы
@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    categories = Category.objects.all()
    return {"categories": categories, "arg1": arg1, "arg2": arg2}
