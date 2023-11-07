from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NewsEntry(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    news_type = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    media_content = models.JSONField(null=True, blank=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
