import logging
import logging.handlers
from multiprocessing import Queue
import os
from dotenv import load_dotenv
import logging_loki
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from textquerycrawlers.textquerycrawlers.spiders.getLatestNews import GetLatestNews


def startCrawling(
    allowed_domains,
    start_urls,
    url,
    css_all_newsdiv,
    title_css,
    pub_date_css,
    body_css,
    image_xpath,
):
    logging.getLogger("requests").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)

    load_dotenv()

    handler = logging_loki.LokiQueueHandler(
        Queue(maxsize=-1),
        url=os.getenv("LOKI_URL"),
        tags={"application": "TextQuery"},
        auth=(os.getenv("LOKI_USER"), os.getenv("LOKI_PASSWORD")),
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

    GetLatestNews.allowed_domains.append(allowed_domains)
    GetLatestNews.start_urls.append(start_urls)
    GetLatestNews.url = url
    GetLatestNews.css_all_newsdiv = css_all_newsdiv
    GetLatestNews.title_css = title_css
    GetLatestNews.pub_date_css = pub_date_css
    GetLatestNews.body_css = body_css
    GetLatestNews.image_xpath = image_xpath

    # Set up crawler
    process = CrawlerProcess(settings)
    process.crawl(GetLatestNews)
    process.start()
