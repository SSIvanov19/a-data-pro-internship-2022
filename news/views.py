from news.models import Entity, News, NewsImage
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.


def remove_dupes(my_list):
    newlist = [my_list[0]]
    for e in my_list:
        flag = True
        for e2 in newlist:
            if e2.name == e.name:
                flag = False
                break

        if flag:
            newlist.append(e)

    return newlist


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"
    paginate_by = 10
    # queryset = News.objects.order_by("-pub_date")

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        sort = self.request.GET.get("sortby")
        order = self.request.GET.get("order")
        object_list = News.objects.order_by("-pub_date")

        if query:
            object_list = News.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )

        if sort and order:
            if order == "asc":
                object_list = object_list.order_by(sort)
            else:
                object_list = object_list.order_by("-" + sort)

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # entities = self.object_list
        entities = Entity.objects.filter(news__in=self.object_list)

        if not entities:
            return context

        for entity in entities:
            entity.count = entities.filter(name=entity.name).count()

        context["entity_list"] = sorted(
            remove_dupes(entities), key=lambda x: x.count, reverse=True
        )

        return context


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
        context["entities"] = sorted(
            remove_dupes(entities), key=lambda x: x.count, reverse=True
        )

        return context
