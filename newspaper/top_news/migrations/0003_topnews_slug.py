# Generated by Django 5.0.6 on 2024-07-14 06:59

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_news', '0002_alter_topnews_topnews_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='topnews',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='topNews_heading', unique=True),
        ),
    ]
