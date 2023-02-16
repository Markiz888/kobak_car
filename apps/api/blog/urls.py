from django.urls import path
from apps.api.blog.views import ArticleSerializer
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register('category', ArticleSerializer, basename='category')

urlpatterns += router.urls
