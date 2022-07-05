from multiprocessing import Pool
from time import sleep
from django.apps import AppConfig
from textquerycrawlers.textquerycrawlers.startCrawling import startCrawling


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"

    def ready(self):
        try:
            # Start crawling in a separate
            pool = Pool(processes=1)
            pool.apply_async(startCrawling)
        except Exception as e:
            print(e)
