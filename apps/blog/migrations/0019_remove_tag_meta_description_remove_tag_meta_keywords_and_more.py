# Generated by Django 4.1.3 on 2023-01-10 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_article_meta_description_article_meta_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='meta_title',
        ),
    ]
