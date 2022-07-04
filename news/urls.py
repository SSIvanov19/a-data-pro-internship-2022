from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path("", views.NewsListView.as_view(), name="index"),
    path("<int:pk>/", views.NewsDetailView.as_view(), name="detail"),
]
