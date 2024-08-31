import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mySpider04.items import ReadBookItem



# 新建项目指令：scrapy startproject mySpider
# 生成爬虫指令，在mySpider/spider目录下：scrapy genspider -t crawl dushu "dushu.com"
# 运行爬虫指令，在mySpider/spider目录下：scrapy crawl itheima
# scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：
# 在mySpider/spider目录下
# scrapy crawl itheima -o teachers.json
# scrapy crawl itheima -o teachers.jsonl
# scrapy crawl itheima -o teachers.csv
# scrapy crawl itheima -o teachers.xml
class DushuSpider(CrawlSpider):
    name = "dushu"
    allowed_domains = ["dushu.com"]
    # 注意第一页也要符合正则表达式
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    # LinkExtractor 链接提取器
    # follow=True 是否跟进 就是其他页按找提取规则进行提出
    # follow=Flse 只提取第一页上的连接
    rules = (Rule(LinkExtractor(allow=r"/book/1188_\d+\.html"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        # item = {}
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        # return item

        print("++++++++++++++++++++++++++++")
        img_list = response.xpath('//div[@class="bookslist"]//li/div[@class="book-info"]//a//img')
        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()

            book = ReadBookItem(name=name, src=src)

            # 获取一个book将book交给pipelines
            yield book
