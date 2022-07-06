from asyncio.log import logger
from cgitb import handler
import imp
import logging
import scrapy
import w3lib.html
from textquerycrawlers.textquerycrawlers.items import NewsItem
import logging


class GetLatestNews(scrapy.Spider):
    name = "getLatestNews"
    allowed_domains = []
    start_urls = []
    url = ""
    css_all_newsdiv = ""
    title_css = ""
    pub_date_css = ""
    body_css = ""
    image_xpath = ""

    def parse_news(self, response):
        logging.info("Getting news from: " + response.url)

        news = NewsItem
        news = {
            "title": response.css(self.title_css).get(),
            "url": response.url,
            "pub_date": response.css(self.pub_date_css).get(),
            "body": "",
            "imageUrl": [],
            "site": self.allowed_domains[0],
        }

        newsBody = ""

        for newsBodyPart in response.css(self.body_css):
            newsBody += (
                " ".join(w3lib.html.remove_tags(newsBodyPart.get()).split()) + "<br>"
            )

        news.update({"body": newsBody})

        if response.xpath(self.image_xpath).extract():
            news["imageUrl"].append(
                self.url + response.xpath(self.image_xpath).extract()[0]
            )

        yield news

    def parse(self, response):
        logging.getLogger("scrapy").propagate = False

        logging.info("Started crawling for news in " + self.allowed_domains[0])
        logging.info("Found " + str(len(response.css(self.css_all_newsdiv))) + " news")

        # Get all news
        for newsDiv in response.css(self.css_all_newsdiv):
            # Get news href
            yield scrapy.Request(
                newsDiv.css("""a""").attrib["href"], callback=self.parse_news
            )
