from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="home"),
    path('news/<str:news_type>/', views.news_by_type, name='news_by_type'),
    path('user_news/', views.user_news, name='user_news'),
    path('create/', views.NewsEntryCreateView.as_view(), name='news-entry-create'),
    path('news/<int:pk>/edit/', views.NewsEntryUpdateView.as_view(),
         name='news-entry-update'),
    path('news/<int:pk>/delete/', views.NewsEntryDeleteView.as_view(),
         name='news-entry-delete'),
]
