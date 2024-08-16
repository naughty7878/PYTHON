import urllib.request


def atest01():
    url = 'http://www.baidu.com'

    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)

    # response = urllib.request.urlopen(request)
    #  1、获取header对象
    header = urllib.request.HTTPHandler()

    #  2、获取opener对象
    opener = urllib.request.build_opener(header)

    #  3、调用open方法
    response = opener.open(request)

    content = response.read().decode('utf-8')
    print(content)


if __name__ == '__main__':
    atest01()