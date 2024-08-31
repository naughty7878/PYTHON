import scrapy

from mySpider03.items import MovieItem


# 新建项目指令：scrapy startproject mySpider
# 生成爬虫指令，在mySpider/spider目录下：scrapy genspider itheima "itheima.com"
# 运行爬虫指令，在mySpider/spider目录下：scrapy crawl itheima
# scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：
# 在mySpider/spider目录下
# scrapy crawl itheima -o teachers.json
# scrapy crawl itheima -o teachers.jsonl
# scrapy crawl itheima -o teachers.csv
# scrapy crawl itheima -o teachers.xml
class Dytt8Spider(scrapy.Spider):
    name = "dytt8"
    allowed_domains = ["dytt8.net"]
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 要第一页的名字 和 第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]/ul//table//tr[2]/td[2]//a[2]')
        print('a_list', a_list)
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # print('href', href)

            # 第二页地址
            link = 'https://www.dytt8.net' + href

            # print('link', link)
            # 对第二页进行访问
            # meta属性字典类型，可以传值
            yield scrapy.Request(url=link, callback=self.parse_second, meta={'name':name})

        # MovieItem
        # print(response.text)

    def parse_second(self, response):
        img = response.xpath('//div[@class="co_content8"]//div[@id="Zoom"]//img')
        # print(img.xpath('./@src').extract_first())
        # 接收请求中的mata参数的值 response.meta
        name = response.meta['name']
        url = img.xpath('./@src').extract_first()

        movie = MovieItem(name=name, url=url)

        yield movie