from django.contrib import admin
from apps.blod.models import BlogCategory
from apps.blod.models import Articl
from apps.blod.models import Tag




admin.site.register(BlogCategory)
admin.site.register(Tag)
admin.site.register(Articl)
