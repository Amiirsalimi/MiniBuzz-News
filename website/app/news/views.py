from django.shortcuts import render
from .models import NewsEntry
from random import randint
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import NewsEntryForm



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
            news['url'] = media_content[random_num].get('url')
    return top_news

def select_image(top_news):
    for news in top_news:
        media_content = news.get('media_content')
        if media_content:
            random_num = randint(0, len(media_content)-1)
            news['url'] = media_content[random_num].get('url')
    return top_news

# Create your views here.
def home(request):
    top_news = NewsEntry.objects.order_by('-published')[:7].values()
    top_news = add_url(top_news)
    hightlight = NewsEntry.objects.order_by('-created_at')[:3].values()
    hightlight = add_url(hightlight)
    return render(request, "news/home.html", context={"top_news":top_news, "hightlight":hightlight})


def news_by_type(request, news_type):
    # Query NewsEntry objects with the given news_type
    news_data = NewsEntry.objects.filter(news_type=news_type).order_by('-published').values()
    news_data = add_url(news_data)
    # Create a Paginator instance with a specified number of items per page
    items_per_page = 10  # You can adjust this to your preferred number of items per page
    paginator = Paginator(news_data, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    # Get the page content for the specified page number
    news_entries_page = paginator.get_page(page)
    context = {
        'news_type': news_type,
        'news_data': news_entries_page,
    }
    
    return render(request, "news/news.html", context)
class NewsEntryListView(ListView):
    model = NewsEntry
    template_name = 'news_entry_list.html'

class NewsEntryCreateView(LoginRequiredMixin, CreateView):
    model = NewsEntry
    template_name = 'news/news_entry_form.html'
    success_url = reverse_lazy('news:home')
    form_class = NewsEntryForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class NewsEntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = NewsEntry
#     template_name = 'news_entry_form.html'
#     form_class = NewsEntryForm
    
#     def test_func(self):
#         return self.get_object().user == self.request.user


# class NewsEntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = NewsEntry
#     template_name = 'news_entry_confirm_delete.html'
#     success_url = reverse_lazy('news-entry-list')
    
#     def test_func(self):
#         return self.get_object().user == self.request.user
