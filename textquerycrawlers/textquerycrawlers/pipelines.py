# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single
import string
import django

django.setup()


from news.models import Entity, News, NewsImage
from textquerycrawlers.textquerycrawlers.items import NewsItem
from dotenv import load_dotenv
import os
import spacy
import w3lib


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

        item["body"] = w3lib.html.remove_tags(item["body"]).translate(
            str.maketrans("", "", string.punctuation)
        )
        # Create entities
        nlp = spacy.load("mk_core_news_md")
        doc = nlp(item["body"])

        for i in doc.ents:
            if i.label_ == "PERSON":
                entity = Entity(name=i.text, news=news)
                entity.save()

        return item
