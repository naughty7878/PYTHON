# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import requests
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道的话，必须在settings中开启管道
class Myspider02Pipeline:
    # 在爬虫文件执行之前执行
    def open_spider(self, spider):
        print("+++++++++++++++++++++++")
        self.fp = open('book.json', 'a', encoding='utf-8')

    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下操作会多次打开文件，不推荐
        # print('process_item',item)
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     # write方法必须是字符串
        #     fp.write(str(item))

        self.fp.write(str(item))

        return item

    # 在爬虫文件执行之后执行
    def close_spider(self, spider):
        print("-------------------")
        self.fp.close()

# 多条管道同时开启
# "mySpider02.pipelines.Myspider02MultiPipeline": 301,
class Myspider02MultiPipeline:
    def process_item(self, item, spider):

        url = 'http:' + item.get('img')
        # print('url', url)
        save_path = './books/' + item.get('name') + '.jpg'
        # print('save_path', save_path)
        self.download_image(url=url, save_path=save_path)

        return item

    def download_image(self, url, save_path):
        try:
            # 发送 GET 请求
            response = requests.get(url, stream=True)

            # 检查请求是否成功
            response.raise_for_status()

            # 确保文件夹存在
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # 以二进制写模式打开文件
            with open(save_path, 'wb') as file:
                # 逐块写入文件
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"图片已成功下载到: {save_path}")

        except requests.RequestException as e:
            print(f"下载图片时发生错误: {e}")
