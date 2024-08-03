import requests


def test01():
    # 发送请求
    resp = requests.get('http://www.baidu.com')
    # 响应状态
    print('响应状态', resp.status_code)
    # 响应状态的描述
    print('响应状态描述', resp.reason)
    # 返回编码
    print('响应编码', resp.apparent_encoding)
    # 响应头
    print('响应头', resp.headers)
    # 响应内容，二进制格式表示
    print('响应内容', '二进制格式', resp.content)
    # 响应内容，字符串格式表示
    print('响应内容', '字符串格式', resp.text)


def test02():
    # 发送请求
    resp = requests.get('https://www.runoob.com/try/ajax/json_demo.json')
    # 响应状态
    print('响应状态', resp.status_code)
    # 响应状态的描述
    print('响应状态描述', resp.reason)
    # 返回编码
    print('响应编码', resp.apparent_encoding)
    # 响应头
    print('响应头', resp.headers)
    # 响应内容，二进制格式表示
    print('响应内容', '二进制格式', resp.content)
    # 响应内容，字符串格式表示
    print('响应内容', '字符串格式', resp.text)
    # 响应内容，json
    json = resp.json()
    print(type(json))
    print('响应内容', 'json格式', json)


def test03():
    # 发送请求
    resp = requests.request('get', 'https://www.runoob.com/')
    # 响应状态
    print('响应状态', resp.status_code)
    # 响应状态的描述
    print('响应状态描述', resp.reason)
    # 返回编码
    print('响应编码', resp.apparent_encoding)
    # 响应头
    print('响应头', resp.headers)
    # 响应内容，二进制格式表示
    # print('响应内容', '二进制格式', resp.content)
    # 响应内容，字符串格式表示
    print('响应内容', '字符串格式', resp.text)


def test04():
    kw = {'s': 'python 教程'}
    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # 发送请求
    resp = requests.get('https://www.runoob.com/', params=kw, headers=headers)
    # 响应状态
    print('响应状态', resp.status_code)
    # 响应状态的描述
    print('响应状态描述', resp.reason)
    # 返回编码
    print('响应编码', resp.apparent_encoding)
    # 响应头
    print('响应头', resp.headers)
    # 响应内容，二进制格式表示
    # print('响应内容', '二进制格式', resp.content)
    # 响应内容，字符串格式表示
    print('响应内容', '字符串格式', resp.text)


def test05():
    # 发送请求
    resp = requests.post('https://www.runoob.com/try/ajax/demo_post.php')
    # 响应状态
    print('响应状态', resp.status_code)
    # 响应状态的描述
    print('响应状态描述', resp.reason)
    # 返回编码
    print('响应编码', resp.apparent_encoding)
    # 响应头
    print('响应头', resp.headers)
    # 响应内容，二进制格式表示
    # print('响应内容', '二进制格式', resp.content)
    # 响应内容，字符串格式表示
    print('响应内容', '字符串格式', resp.text)


if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    test05()