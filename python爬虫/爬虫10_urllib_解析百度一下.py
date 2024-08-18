import urllib.request
from lxml import etree

url = 'https://www.baidu.com/'

headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 请求对象的定制
request = urllib.request.Request(url, None, headers)

# 访问服务器
response = urllib.request.urlopen(request)

# 获取源码
content = response.read().decode('utf8')
print(content)

# 解析
tree = etree.HTML(content
                  )
# 查询对应元素，xpath的返回值是一个列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')
print('~' * 30)
print('result', result)
