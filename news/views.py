from multiprocessing import Pool
from crawlers.models import Crawler
from news.models import Entity, News, NewsImage
from django.views.generic import ListView, DetailView
from django.db.models import Q

from textquerycrawlers.textquerycrawlers.startCrawlingSpecific import (
    startCrawlingSpecific,
)

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
    paginate_by = 12

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        sort = self.request.GET.get("sortby")
        order = self.request.GET.get("order")
        crawl = self.request.GET.get("crawl")
        object_list = News.objects.order_by("-pub_date")

        if crawl == "true" and query:
            try:
                # Start crawling in a separate
                crawlers = Crawler.objects.all()
                for crawler in crawlers:
                    print(crawler.allowed_domain)
                    pool = Pool(processes=1)
                    pool.apply_async(
                        startCrawlingSpecific,
                        args=(
                            crawler.allowed_domain,
                            crawler.start_url_search,
                            crawler.url,
                            crawler.css_search_newsdiv,
                            crawler.title_css,
                            crawler.pub_date_css,
                            crawler.body_css,
                            crawler.image_xpath,
                            query,
                        ),
                    )
            except Exception as e:
                print(e)

        if query:
            object_list = News.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )

        if sort and order:
            if order == "asc":
                object_list = object_list.order_by(sort)
            else:
                object_list = object_list.order_by("-" + sort)

        # Add imageurl to object_list
        for news in object_list:
            if NewsImage.objects.filter(news=news).first():
                news.imageurl = NewsImage.objects.filter(news=news).first().image_url

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

        if not entities:
            return context

        for entity in entities:
            entity.count = entities.filter(name=entity.name).count()

        context["entities"] = sorted(
            remove_dupes(entities), key=lambda x: x.count, reverse=True
        )

        return context
