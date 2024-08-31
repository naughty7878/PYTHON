# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Myspider03Pipeline:

    # 在爬虫文件执行之前执行
    def open_spider(self, spider):
        print('在爬虫文件执行之前执行')
        self.fp = open('movie.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行之后执行
    def close_spider(self, spider):
        print('在爬虫文件执行之后执行')
        self.fp.close()