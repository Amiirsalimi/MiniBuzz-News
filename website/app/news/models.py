from django.db import models

# Create your models here.

class NewsEntry(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    media_content = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title
