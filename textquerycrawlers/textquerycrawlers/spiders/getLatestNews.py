import imp
import logging
import scrapy
import w3lib.html
import sys

from textquerycrawlers.textquerycrawlers.items import NewsItem


class GetLatestNews(scrapy.Spider):
    name = "getLatestNews"
    allowed_domains = ["gov.bg"]
    start_urls = ["https://gov.bg/bg/prestsentar/novini"]

    def parse_news(self, response):
        news = NewsItem
        news = {
            "title": response.css(""".view > h1:nth-child(2)::text""").get(),
            "url": response.url,
            "pub_date": response.css(""".view > p:nth-child(3)::text""").get(),
            "body": "",
            "imageUrl": [],
            "site": "gov.bg",
        }

        newsBody = ""

        for newsBodyPart in response.css(""".view > p"""):
            newsBody += (
                " ".join(w3lib.html.remove_tags(newsBodyPart.get()).split()) + "<br>"
            )

        news.update({"body": newsBody})
        news["imageUrl"].append(
            "https://gov.bg"
            + response.xpath("""//*[@id="lightgallery"]/li/img/@src""").extract()[0]
        )

        yield news

    def parse(self, response):
        logging.getLogger("scrapy").propagate = False
        # Get all news
        for newsDiv in response.css("""div.item"""):
            # Get news href
            yield scrapy.Request(
                newsDiv.css("""a""").attrib["href"], callback=self.parse_news
            )
