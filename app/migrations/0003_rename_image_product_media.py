# Generated by Django 5.1.3 on 2024-12-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='media',
        ),
    ]
