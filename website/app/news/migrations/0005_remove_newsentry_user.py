# Generated by Django 4.1.7 on 2023-11-07 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsentry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsentry',
            name='user',
        ),
    ]
