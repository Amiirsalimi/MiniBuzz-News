from django.contrib import admin
from .models import NewsEntry
from django.utils import timezone

# Register your models here.
# admin.site.register(NewsEntry)


from django.contrib import admin
from .models import NewsEntry
import feedparser
import json
from datetime import datetime


def fetch_and_save_news(modeladmin, request, queryset):
    # Your script to fetch and save the news data here
    # This code assumes that you have already defined the script.

    # Example code to fetch and save news data from the feed
    feed = feedparser.parse('http://rss.cnn.com/rss/edition_world.rss')
    for entry in feed.get('entries', []):
        try:
            published_date = datetime.strptime(entry.get("published"), "%a, %d %b %Y %H:%M:%S %Z")
        except:
            published_date = None
            
        title = entry.get("title")
        # Check if a NewsEntry with the same title already exists
        existing_entry = NewsEntry.objects.filter(title=title).first()

        if not existing_entry:
            NewsEntry.objects.create(
                title=title,
                link=entry.get("link"),
                published=published_date,
                summary=entry.get("summary"),
                media_content=entry.get('media_content', [])
            )

    modeladmin.message_user(request, "News data has been fetched and saved successfully.")

fetch_and_save_news.short_description = "Fetch and Save News Data"

class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
    actions = [fetch_and_save_news]

admin.site.register(NewsEntry, NewsEntryAdmin)
