from django.urls import path
from apps.api.blog.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('category', ArticleViewSet, basename='category')

urlpatterns += router.urls
