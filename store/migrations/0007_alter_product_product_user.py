# Generated by Django 4.1.7 on 2023-03-09 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_alter_product_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p_user', to=settings.AUTH_USER_MODEL),
        ),
    ]