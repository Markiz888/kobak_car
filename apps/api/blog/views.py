from rest_framework import generics, permissions, viewsets
from apps.blog.models import Article, BlogCategory, Tag
from apps.api.blog.serializers import ArticleSerializer
class ProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update' 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]