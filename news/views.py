from django.shortcuts import render
from news.models import News
from django.views.generic import ListView

# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"
    paginate_by = 10
    queryset = News.objects.order_by("-pub_date")
