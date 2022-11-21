from django.contrib import admin
from apps.blog.models import BlogCategory
from apps.blog.models import Articl
from apps.blog.models import Tag




admin.site.register(BlogCategory)
admin.site.register(Tag)
admin.site.register(Articl)
