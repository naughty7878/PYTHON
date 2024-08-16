import urllib.request
import urllib.parse
import json


def atest01():
    url = 'https://www.baidu.com/s?wd='

    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    # 将中文转unicode编码
    name = urllib.parse.quote('周杰伦')
    print(name)

    # 请求对象定制
    request = urllib.request.Request(url + name, None, headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')
    print(content)


def atest02():
    data = {
        'wd': '周杰伦',
        'sex': '男'
    }

    a = urllib.parse.urlencode(data)
    print(a)  # wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7


def atest03():
    data = {
        'wd': '周杰伦',
        'sex': '男'
    }

    # UA反爬
    url = 'https://www.baidu.com/s?'

    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    # 请求对象定制
    request = urllib.request.Request(url + urllib.parse.urlencode(data), None, headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')
    print(content)


def atest04():
    url = 'https://fanyi.baidu.com/sug'

    # UA反爬
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    data = {
        'kw': 'spider'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    # 请求对象定制
    request = urllib.request.Request(url, data, headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')
    print(content)
    obj = json.loads(content)
    print(obj)




atest04()
