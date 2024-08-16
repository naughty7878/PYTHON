import urllib.request


url = 'http://www.baidu.com'


# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# HTTPResponse
print(type(response))

print(response)
print(response.status)
print(response.getcode())
print(response.geturl())
print(response.getheaders())

# 读取数据
# # 读取所有数据
# content = response.read().decode('utf-8')
# print(content)
#
# # 读取一行
# content = response.readline().decode('utf-8')
# print(content)

# 读取多行
content = response.readlines()
for i in content:
    print(i.decode('utf-8'))
