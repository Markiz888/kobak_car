from django.urls import reverse
from django.shortcuts import render

from apps.blog.models import BlogCategory, Article, Tag, Comment
from apps.blog.forms import CommentForm


# Create your views here.
def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': 'Блог'}
    return render(request, 'blog/category_list.html', {"categories": blog_categories, 'breadcrumbs': breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': category.name
    }
    return render(request,
                  'blog/article_list.html', {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article, is_checked=True)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        reverse('blog_article_list', args=[category_id]): category.name,
        'current': article.title
    }
    return render(request,
                  'blog/article_view.html', {
                      "category": category,
                      "article": article,
                      'breadcrumbs': breadcrumbs,
                      'comments': comments})


def tag_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': tag.name
    }
    return render(request, 'blog/tag_view.html', {'tag': tag, 'articles': articles, 'breadcrumbs': breadcrumbs})

def create_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article_id)

        if not request.user.is_anonymous:
            user = request.user
            data.update({"name": f"{user.last_name} {user.first_name}",
                         "is_checked": True,
                         "email": user.email,
                         "user": user})

        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            breadcrumbs = {'current': 'Комментарий успешно добавлен'}
            return render(request, 'blog/comment_created.html', {
                "comment": comment,
                "breadcrumbs": breadcrumbs,
                "article": article})
