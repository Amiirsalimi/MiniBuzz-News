from django.shortcuts import render
from .models import NewsEntry
# Create your views here.
def home(request):
    top_news = NewsEntry.objects.all()[:3]
    return render(request, "news/home.html", context={"top_news":top_news})