from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="home"),
    # path('', views.ActivityListCreateView.as_view(), name='news_list'),


]
