# Generated by Django 5.1.3 on 2024-12-09 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_image_product_media'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_oder',
            new_name='date_order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='oder',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='oder',
            new_name='order',
        ),
    ]