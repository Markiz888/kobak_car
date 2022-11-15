# Generated by Django 4.1.3 on 2022-11-15 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blod', '0002_rename_blogcategorymodel_blogcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text_previes', models.TextField(blank=True, null=True, verbose_name='Текст-привью')),
                ('text', models.TextField(verbose_name='Текст')),
                ('publish_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('uppdated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('categore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blod.blogcategory')),
            ],
            options={
                'verbose_name': 'Ствтья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
