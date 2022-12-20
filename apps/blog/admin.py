from django.contrib import admin
from apps.blog.models import BlogCategory, Tag, Article
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode


admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_count']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image']
    readonly_fields = ['image_tag']

    def article_count(self, instance):
        articles = Article.objects.filter(category=instance).count()
        url = reverse('admin:blog_article_changelist') + '?' + urlencode({'category__id__exact': instance.id})
        return format_html(f"<a href='{url}'>Статей: {articles}</a>")

    article_count.short_description = 'Статей'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','category_link','publish_date','created_at']
    list_display_links = ['id', 'title']
    list_filter = ['category', 'tags']

    def category_link(self, instance):
        url = reverse('admin:blog_blogcategory_change', args=[instance.category_id])
        return format_html(f"<a href='{url}'>{instance.category.name}</a>")

    category_link.short_description = 'Категория'
