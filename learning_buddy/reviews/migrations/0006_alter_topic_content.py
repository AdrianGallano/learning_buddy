# Generated by Django 5.0.3 on 2024-03-24 13:17

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_remove_topic_path_topic_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=tinymce.models.HTMLField(default='', null=True),
        ),
    ]