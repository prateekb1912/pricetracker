# Generated by Django 4.1.4 on 2023-02-07 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_alter_product_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='asin',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sell_price',
            new_name='price',
        ),
    ]
