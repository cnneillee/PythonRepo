# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Category(Item):
    name = Field()
    url = Field()
    articleNum = Field()


class Article(Item):
    url = Field()
    title = Field()
    date = Field()
    categories = Field()
    tags = Field()
    content = Field()
    readNum = Field()

