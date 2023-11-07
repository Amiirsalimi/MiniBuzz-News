from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="home"),
    path('news/<str:news_type>/', views.news_by_type, name='news_by_type'),
]
