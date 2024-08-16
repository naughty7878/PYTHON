import urllib.request

url = 'https://www.baidu.com'

headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

# 请求对象定制
request = urllib.request.Request(url, None, headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)
