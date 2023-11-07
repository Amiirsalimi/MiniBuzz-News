from django.shortcuts import render
from .models import NewsEntry
from random import randint


def filter_media_images(media_content):
    filter_media = []
    for media in media_content:
        if media.get('height') and media.get('width'):
            if media.get('height') < media.get('width'):
                filter_media.append(media)
    return filter_media

def add_url(top_news):
    for news in top_news:
        media_content = news.get('media_content')
        if media_content:
            media_content = filter_media_images(media_content)
            random_num = randint(0, len(media_content)-1)
            print(media_content[random_num])
            news['url'] = media_content[random_num].get('url')
    return top_news

# Create your views here.
def home(request):
    top_news = NewsEntry.objects.order_by('-published')[:7].values()
    top_news = add_url(top_news)
    hightlight = NewsEntry.objects.order_by('-created_at')[:3].values()
    hightlight = add_url(hightlight)
    return render(request, "news/home.html", context={"top_news":top_news, "hightlight":hightlight})


