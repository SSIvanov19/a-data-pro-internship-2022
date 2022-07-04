from django.apps import AppConfig
from textquerycrawlers.textquerycrawlers.startCrawling import startCrawling

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        startCrawling()
