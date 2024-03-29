# Generated by Django 5.0.1 on 2024-03-17 16:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='date_time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='date_time_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
