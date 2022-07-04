import os
import logging
import logging.handlers
from multiprocessing import Queue
from dotenv import load_dotenv
from pathlib import Path
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from textquerycrawlers.textquerycrawlers.spiders.getLatestNews import GetLatestNews


def startCrawling():
    # Set up Scrapy settings
    settings = get_project_settings()
    settings["ITEM_PIPELINES"] = {
        "textquerycrawlers.textquerycrawlers.pipelines.TextquerycrawlersPipeline": 300,
    }

    # Set up crawler
    process = CrawlerProcess(settings)
    process.crawl(GetLatestNews)
    process.start()
