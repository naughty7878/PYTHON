import urllib.request
from bs4 import BeautifulSoup

url = 'https://sc.chinaz.com/tag_tupian/yazhoumeinu.html'

headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

soup = BeautifulSoup(content, 'lxml');
# print(soup)
# src_list = tree.xpath("//div[@class='item masonry-brick']/img[@class='lazy']/@src")
# name_list = tree.xpath("//div[@class='item masonry-brick']/img[@class='lazy']/@alt")
# if len(src_list) == 0:
#     src_list = tree.xpath("//div[@class='item']/img[@class='lazy']/@data-original")
#     name_list = tree.xpath("//div[@class='item']/img[@class='lazy']/@alt")

img_list = soup.select('div[class="item masonry-brick"] img[class="lazy"]')
if len(img_list) == 0:
    img_list = soup.select('div[class="item"] img[class="lazy"]')

for img in img_list:
    print(img.get('alt'), img.get('data-original'))
#

#
# obj = json.load(open('爬虫13-urllib-解析jsonpath淘票票.json', 'r', encoding='utf-8'))
#
# city_list = jsonpath.jsonpath(obj, '$..regionName')
# print(city_list)