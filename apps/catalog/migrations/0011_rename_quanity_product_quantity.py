# Generated by Django 4.1.3 on 2023-01-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_productimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quanity',
            new_name='quantity',
        ),
    ]