from news.models import Entity, News, NewsImage
from django.views.generic import ListView, DetailView

# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"
    paginate_by = 10
    queryset = News.objects.order_by("-pub_date")


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_images"] = NewsImage.objects.filter(news=self.object)

        entities = Entity.objects.filter(news=self.object)
        for entity in entities:
            entity.count = entities.filter(name=entity.name).count()
        context["entities"] = entities

        return context
