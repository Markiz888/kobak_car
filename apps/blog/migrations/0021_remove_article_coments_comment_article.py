# Generated by Django 4.1.3 on 2023-02-27 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_comment_article_coments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='coments',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='Статья'),
            preserve_default=False,
        ),
    ]
