# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
# 加载setting文件
from scrapy.utils.project import get_project_settings


class Myspider04Pipeline:
    # 在爬虫文件执行之前执行
    def open_spider(self, spider):
        print('在爬虫文件执行之前执行')
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行之后执行
    def close_spider(self, spider):
        print('在爬虫文件执行之后执行')
        self.fp.close()


class MySQLPipeline:
    # 在爬虫文件执行之前执行
    def open_spider(self, spider):
        print('MySQLPipeline在爬虫文件执行之前执行')
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.database = settings['DB_DATABASE']
        self.charset = settings['DB_CHARSET']
        # 连接
        self.connect()

    def connect(self):
        # 打开数据库连接
        self.connect = pymysql.connect(host=self.host, port=self.port,
                                       user=self.user, password=self.password,
                                       database=self.database, charset=self.charset)
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 插入数据
        self.insert_data(item)
        return item

    # 在爬虫文件执行之后执行
    def close_spider(self, spider):
        print('MySQLPipeline在爬虫文件执行之后执行')
        # 关闭数据库连接
        self.connect.close()

    def insert_data(self, item):

        # SQL 插入语句
        sql = f"""INSERT INTO `book` (`name`, `url`) 
            VALUES ('{item['name']}', '{item['src']}')"""
        print('sql', sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.connect.commit()
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.connect.rollback()

