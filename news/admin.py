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
news_rss = [
    {"Top Stories":     "http://rss.cnn.com/rss/edition.rss"},
    {"World": 		    "http://rss.cnn.com/rss/edition_world.rss"},
    {"Africa": 		    "http://rss.cnn.com/rss/edition_africa.rss"},
    {"Americas": 	    "http://rss.cnn.com/rss/edition_americas.rss"},
    {"Asia": 		    "http://rss.cnn.com/rss/edition_asia.rss"},
    {"Europe": 		    "http://rss.cnn.com/rss/edition_europe.rss"},
    {"Middle East":     "http://rss.cnn.com/rss/edition_meast.rss"},
    {"U.S.": 		    "http://rss.cnn.com/rss/edition_us.rss"},
    {"Money": 		    "http://rss.cnn.com/rss/money_news_international.rss"},
    {"Technology": 		"http://rss.cnn.com/rss/edition_technology.rss"},
    {"Science & Space": "http://rss.cnn.com/rss/edition_space.rss"},
    {"Entertainment": 	"http://rss.cnn.com/rss/edition_entertainment.rss"},
    {"World Sport": 	"http://rss.cnn.com/rss/edition_sport.rss"},
    {"Football": 		"http://rss.cnn.com/rss/edition_football.rss"},
    {"Golf": 		    "http://rss.cnn.com/rss/edition_golf.rss"},
    {"Motorsport": 		"http://rss.cnn.com/rss/edition_motorsport.rss"},
    {"Tennis":		    "http://rss.cnn.com/rss/edition_tennis.rss"},
    {"Travel": 		    "http://rss.cnn.com/rss/edition_travel.rss"},
    {"Video": 		    "http://rss.cnn.com/rss/cnn_freevideo.rss"},
    {"Most Recent": 	"http://rss.cnn.com/rss/cnn_latest.rss"},
]


def fetch_and_save_news(modeladmin, request, queryset):
    # Your script to fetch and save the news data here
    # This code assumes that you have already defined the script.
    for each_news_type in news_rss:
        for key, value in each_news_type.items():
            print(key, value)
            feed = feedparser.parse(value)
            for entry in feed.get('entries', []):
                try:
                    published_date = datetime.strptime(
                        entry.get("published"), "%a, %d %b %Y %H:%M:%S %Z")
                except:
                    published_date = None

                title = entry.get("title")
                # Check if a NewsEntry with the same title already exists
                existing_entry = NewsEntry.objects.filter(title=title).first()

                if not existing_entry:
                    NewsEntry.objects.create(
                        title=title,
                        news_type=key,
                        link=entry.get("link"),
                        published=published_date,
                        summary=entry.get("summary"),
                        media_content=entry.get('media_content', [])
                    )

    modeladmin.message_user(
        request, "News data has been fetched and saved successfully.")


fetch_and_save_news.short_description = "Fetch and Save News Data"


class NewsEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
    actions = [fetch_and_save_news]


admin.site.register(NewsEntry, NewsEntryAdmin)
