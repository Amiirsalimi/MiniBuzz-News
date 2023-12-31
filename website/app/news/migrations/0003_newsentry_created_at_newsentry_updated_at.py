# Generated by Django 4.1.7 on 2023-11-05 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsentry_news_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsentry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsentry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
