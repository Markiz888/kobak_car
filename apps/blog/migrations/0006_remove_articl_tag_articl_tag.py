# Generated by Django 4.1.3 on 2022-11-17 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_tag_alter_articl_options_articl_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articl',
            name='tag',
        ),
        migrations.AddField(
            model_name='articl',
            name='tag',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]