import scrapy

from mySpider02.items import DangDangItem


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.01.02.00.00.00.html"]

    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items  定义数据结构
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 第一张
            # img = li.xpath('.//img/@src')[0].extract()
            # # 之后的
            # img = li.xpath('.//img/@data-original')[0].extract()
            img = li.xpath('.//img/@data-original').extract_first()
            if not img:
                img = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()')[0].extract()
            print(img, name, price)

            book = DangDangItem(img=img, name=name, price=price)

            # 获取一个book将book交给pipelines
            yield book

            #  每一页的爬取的业务逻辑全都是一样的，
            #  所以我们只需要将执行的那个页的请求再次调用parse方法就可以了
            #    http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
            #    http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
            #    http://category.dangdang.com/pg4-cp01.01.02.00.00.00.html

        # 请求其他页
        self.page = self.page + 1
        if self.page <= 3:
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            #  怎么去调用parse方法
            #  scrapy.Request就是scrpay的get请求
            #  url就是请求地址
            #  callback是你要执行的那个函数  注意不需要加（）
            yield scrapy.Request(url=url, callback=self.parse)
