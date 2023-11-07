# Generated by Django 4.1.7 on 2023-11-07 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_newsentry_created_at_newsentry_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsentry',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
