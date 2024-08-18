import urllib.request
from lxml import etree


# url = 'https://www.baidu.com/'
#

#

#

# print(content)
#

# print('~' * 30)
# print('result', result)


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tag_tupian/yazhoumeinu.html'
    else:
        url = f'https://sc.chinaz.com/tag_tupian/yazhoumeinu_{page}.html'
    # print(url)
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    # 请求对象的定制
    request = urllib.request.Request(url, None, headers)

    return request


def get_content(request):
    # 访问服务器
    response = urllib.request.urlopen(request)

    # 获取源码
    content = response.read().decode('utf8')
    return content


def down_load(content):
    # 解析
    tree = etree.HTML(content)
    # 查询对应元素  src alt
    src_list = tree.xpath("//div[@class='item masonry-brick']/img[@class='lazy']/@src")
    name_list = tree.xpath("//div[@class='item masonry-brick']/img[@class='lazy']/@alt")
    if len(src_list) == 0:
        src_list = tree.xpath("//div[@class='item']/img[@class='lazy']/@data-original")
        name_list = tree.xpath("//div[@class='item']/img[@class='lazy']/@alt")
    print('src_list', len(src_list), 'name_list', len(name_list))
    for i in range(len(src_list)):
        url_img = src_list[i]
        name = name_list[i]
        urllib.request.urlretrieve(f'https:{url_img}', f'./图片/{name}.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = create_request(page)
        # 获取页面的源码
        content = get_content(request)
        print(content)
        # 下载图片
        down_load(content)
