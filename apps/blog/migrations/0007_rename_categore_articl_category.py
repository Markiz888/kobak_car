# Generated by Django 4.1.3 on 2022-11-22 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_articl_tag_articl_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articl',
            old_name='categore',
            new_name='category',
        ),
    ]