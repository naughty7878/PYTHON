# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider02Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DangDangItem(scrapy.Item):
    # 名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 图片
    img = scrapy.Field()