# Generated by Django 4.1.3 on 2022-11-22 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_articl_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text_previes',
            new_name='text_preview',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='uppdated_at',
            new_name='updated_at',
        ),
    ]
