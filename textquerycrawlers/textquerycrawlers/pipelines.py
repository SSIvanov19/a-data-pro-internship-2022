# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from news.models import News, NewsImage
from textquerycrawlers.textquerycrawlers.items import NewsItem
from dotenv import load_dotenv
import os

class TextquerycrawlersPipeline:
    def process_item(self, item, spider):
        # Create news
        news = News(
            title=item["title"],
            url=item["url"],
            pub_date=item["pub_date"],
            body=item["body"],
            site=item["site"],
        )
        news.save()

        # Create news images
        for imageUrl in item["imageUrl"]:
            newsImage = NewsImage(news=news, image_url=imageUrl)
            newsImage.save()

        return item
