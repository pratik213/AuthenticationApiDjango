# Generated by Django 4.1.7 on 2023-03-08 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_product_id_product_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='product_user',
        ),
    ]