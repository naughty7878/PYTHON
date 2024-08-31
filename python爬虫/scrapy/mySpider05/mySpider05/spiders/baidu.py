import json
from typing import Iterable

import scrapy
import chardet
from scrapy import Request


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]

    # post请求 如果没有参数 那么这个请求将没有任何意义
    # 所以start_urls 也没有用了
    # parse方法也没有用了
    # start_urls = ['https://fanyi.baidu.com/sug/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }



        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_post)

    def parse_post(self, response):
        self.logger.info('请求地址：%s', response.url)
        content = response.text
        obj = json.loads(content)
        print(obj)
