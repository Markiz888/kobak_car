from django.shortcuts import render
from django.views import generic

from apps.main.models import Page


def index(requst):
    return render(requst, 'index.html')


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()
