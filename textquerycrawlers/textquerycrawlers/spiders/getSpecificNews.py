import logging
import scrapy
import w3lib.html
from textquerycrawlers.textquerycrawlers.items import NewsItem
import logging


class GetSpecificNews(scrapy.Spider):
    name = "getSpecificNews"
    allowed_domains = ["gov.bg"]
    start_urls = ["https://gov.bg/bg/search?q="]

    def parse_news(self, response):
        logging.info("Getting news from: " + response.url)

        news = NewsItem
        news = {
            "title": response.css(""".view > h1::text""").get(),
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

        if response.xpath("""//*[@id="lightgallery"]/li/img/@src""").extract():
            news["imageUrl"].append(
                "https://gov.bg"
                + response.xpath("""//*[@id="lightgallery"]/li/img/@src""").extract()[0]
            )

        yield news

    def parse(self, response):
        logging.getLogger("scrapy").propagate = False

        logging.info("Started crawling for news in " + self.allowed_domains[0])
        logging.info(
            "Found "
            + str(len(response.css(""".articles-tabs > ul:nth-child(1) > li""")))
            + " news"
        )

        # Get all news
        for newsDiv in response.css(""".articles-tabs > ul:nth-child(1) > li"""):
            # Get news href
            yield scrapy.Request(
                newsDiv.css("""a""").attrib["href"], callback=self.parse_news
            )
