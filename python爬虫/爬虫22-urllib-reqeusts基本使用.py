import requests

# 发送请求
resp = requests.get('http://www.baidu.com')
# 解决乱码
resp.encoding = 'utf-8'

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


