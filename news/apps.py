from multiprocessing import Pool
from django.apps import AppConfig

from textquerycrawlers.textquerycrawlers.startCrawling import startCrawling


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"

    def ready(self):
        try:
            from crawlers.models import Crawler

            # Start crawling in a separate
            crawlers = Crawler.objects.all()

            for crawler in crawlers:
                pool = Pool(processes=1)
                pool.apply_async(
                    startCrawling,
                    args=(
                        crawler.allowed_domain,
                        crawler.start_url,
                        crawler.url,
                        crawler.css_all_newsdiv,
                        crawler.title_css,
                        crawler.pub_date_css,
                        crawler.body_css,
                        crawler.image_xpath,
                    ),
                )

        except Exception as e:
            print(e)
