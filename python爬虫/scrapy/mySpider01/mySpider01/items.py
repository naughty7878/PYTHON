# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ItheimaItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
