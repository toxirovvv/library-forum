# Generated by Django 5.0.4 on 2024-05-25 08:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Followers', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]