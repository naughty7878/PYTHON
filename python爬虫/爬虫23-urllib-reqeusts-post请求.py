import requests
import json


def send_post_request(url, data, headers=None):
    try:
        # 发送 POST 请求
        response = requests.post(url, data=data, headers=headers)

        # 检查请求是否成功
        response.raise_for_status()

        # 解决乱码
        response.encoding = 'utf-8'

        # 尝试解析 JSON 响应
        try:
            json_response = response.json()
            return json_response
        except json.JSONDecodeError:
            # 如果响应不是 JSON 格式，返回文本内容
            return response.text

    except requests.RequestException as e:
        print(f"发生错误: {e}")
        return None


# 使用示例
url = 'http://fanyi.baidu.com/sug'
data = {
    'ky': 'eye'
}
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'Content-Type': 'application/json'
}

response = send_post_request(url, data, headers)
if response:
    print("响应:", response)



# # 发送请求
# resp = requests.get(url=url, params=data, headers=headers)
# # 解决乱码
# resp.encoding = 'utf-8'
#
# # 响应状态
# print('响应状态', resp.status_code)
# # 响应状态的描述
# print('响应状态描述', resp.reason)
# # 返回编码
# print('响应编码', resp.apparent_encoding)
# # 响应头
# print('响应头', resp.headers)
# # 响应内容，二进制格式表示
# # print('响应内容', '二进制格式', resp.content)
# # 响应内容，字符串格式表示
# print('响应内容', resp.text)


