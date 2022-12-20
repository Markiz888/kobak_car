from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe
from config.settings import MEDIA_ROOT


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=255)
    # image = models.ImageField(verbose_name="Изображение", upload_to="blog/category/", null=True)
    image = ProcessedImageField(
        verbose_name="Изображения",
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категория блога'


    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Изображение'

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Изображения'


class Tag(models.Model):
    name = models.CharField(verbose_name='Tag', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory, verbose_name="категория", on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name="Текст-привью", null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    tags = models.ManyToManyField(Tag)
    image = ProcessedImageField(
        verbose_name="Изображения",
        upload_to='blog/article/',
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    publish_date = models.DateTimeField(verbose_name="Дата публикации")
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
