# Generated by Django 4.1.7 on 2023-03-07 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
