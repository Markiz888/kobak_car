from django.http import HttpResponse


def index(requst):
    return HttpResponse('Привет, это главная страница')
