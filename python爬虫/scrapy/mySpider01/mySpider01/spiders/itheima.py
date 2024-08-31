import scrapy

# 引入item，报错不影响
from mySpider01.items import ItheimaItem

# 新建项目指令：scrapy startproject mySpider
# 生成爬虫指令，在mySpider/spider目录下：scrapy genspider itheima "itheima.com"
# 运行爬虫指令，在mySpider/spider目录下：scrapy crawl itheima
# scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：
# 在mySpider/spider目录下
# scrapy crawl itheima -o teachers.json
# scrapy crawl itheima -o teachers.jsonl
# scrapy crawl itheima -o teachers.csv
# scrapy crawl itheima -o teachers.xml

class ItheimaSpider(scrapy.Spider):
    # 运行爬虫：scrapy crawl itheima
    # 运行爬虫保存数据：scrapy crawl itheima -o teachers.json
    name = "itheima"
    allowed_domains = ["itheima.com"]
    start_urls = ["https://www.itheima.com/teacher.html"]

    def parse(self, response):
        filename = "teacher.html"
        with open(filename, 'w', encoding='utf-8') as fs:
            fs.write(response.text)
        # //div[@id='mCSB_1_container']/ul/li/div[@class='teamain']/div[@class='main_pic']/img[@class='mCS_img_loaded']/@src
        # //div[@id='mCSB_1_container']/ul/li/div[@class='teamain']/div[@class='main_bot']/h2/text()
        # //div[@id='mCSB_1_container']/ul/li/div[@class='teamain']/div[@class='main_bot']/h2/span/text()
        img_list = response.xpath(
            "//div[@class='graybg tea_main']//div[@class='tea_con']//ul/li/img/@src")
        name_list = response.xpath(
            "//div[@class='graybg tea_main']//div[@class='tea_con']//ul/li/div[@class='li_txt']/h3/text()")
        title_list = response.xpath(
            "//div[@class='graybg tea_main']//div[@class='tea_con']//ul/li/div[@class='li_txt']/h4/text()")
        print(name_list)
        # 存放老师信息的集合
        items = []

        for i in range(len(img_list)):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItheimaItem()
            # extract()方法返回的都是unicode字符串
            img = img_list[i]
            name = name_list[i]
            title = title_list[i]


            # xpath返回的是包含一个元素的列表
            item['img'] = img.extract()
            item['name'] = name.extract()
            item['title'] = title.extract()


            items.append(item)

        print(items)

        # 直接返回最后数据
        return items
