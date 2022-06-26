from django.http import HttpResponse

# from .models import News, Category

def index(request):
    return HttpResponse('Hello world')
