from django.shortcuts import render
from django.views import generic

from apps.main.models import Page, ProductSet


def index(requst):
    page = Page.objects.get(slug='home')
    product_sets = ProductSet.objects.filter(is_active=True)
    return render(requst, 'index.html', {'page': page, "product_sets": product_sets})


class PageView(generic.DetailView):
    model = Page
    template_name = 'main/page.html'
    queryset = Page.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'breadcrumbs': {'current': self.object.slug}})

        return context
