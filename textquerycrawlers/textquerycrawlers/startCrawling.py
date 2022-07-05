import logging
import logging.handlers
from multiprocessing import Queue
import logging_loki
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from textquerycrawlers.textquerycrawlers.spiders.getLatestNews import GetLatestNews


def startCrawling():
    logging.getLogger("requests").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)

    handler = logging_loki.LokiQueueHandler(
        Queue(maxsize=-1),
        url="https://empireloki.azurewebsites.net/loki/api/v1/push",
        tags={"application": "TextQuery"},
        auth=("Fiki", "R3pt1l123"),
        version="1",
    )

    # Add handler to the root logger
    logging.basicConfig(level=logging.INFO, handlers=[handler])

    logging.getLogger().addHandler(handler)
    logging.getLogger("root").addHandler(handler)

    # Set up Scrapy settings
    settings = get_project_settings()
    settings["ITEM_PIPELINES"] = {
        "textquerycrawlers.textquerycrawlers.pipelines.TextquerycrawlersPipeline": 300,
    }

    # Set up crawler
    process = CrawlerProcess(settings)
    process.crawl(GetLatestNews)
    process.start()
