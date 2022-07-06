import logging
import logging.handlers
from multiprocessing import Queue
import os
from dotenv import load_dotenv
import logging_loki
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from textquerycrawlers.textquerycrawlers.spiders.getSpecificNews import GetSpecificNews


def startCrawlingSpecific(
    allowed_domains,
    start_url_search,
    url,
    css_search_newsdiv,
    title_css,
    pub_date_css,
    body_css,
    image_xpath,
    newsToSearch,
):
    load_dotenv()

    logging.getLogger("requests").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)

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

    GetSpecificNews.allowed_domains.append(allowed_domains)
    GetSpecificNews.start_urls.append(start_url_search)
    GetSpecificNews.start_urls[0] += newsToSearch
    GetSpecificNews.url = url
    GetSpecificNews.css_search_newsdiv = css_search_newsdiv
    GetSpecificNews.title_css = title_css
    GetSpecificNews.pub_date_css = pub_date_css
    GetSpecificNews.body_css = body_css
    GetSpecificNews.image_xpath = image_xpath

    # Set up crawler
    process = CrawlerProcess(settings)
    process.crawl(GetSpecificNews)
    process.start()
