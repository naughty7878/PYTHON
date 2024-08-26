import json
import os
import chaojiying

import requests
from lxml import etree


def download_image(session, url, save_path):
    try:
        # 发送 GET 请求
        response = session.get(url, stream=True)

        # 检查请求是否成功
        response.raise_for_status()

        # 确保文件夹存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 以二进制写模式打开文件
        with open(save_path, 'wb') as file:
            # 逐块写入文件
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"图片已成功下载到: {save_path}")

    except requests.RequestException as e:
        print(f"下载图片时发生错误: {e}")


def send_get_request(url, params=None, headers=None):
    try:
        # 发送 GET 请求
        response = requests.get(url, params=params, headers=headers)

        # 检查请求是否成功
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text

        # 尝试解析 JSON 响应
        # try:
        #     json_response = response.json()
        #     return json_response
        # except ValueError:
        #     # 如果响应不是 JSON 格式，返回文本内容
        #     return response.text

    except requests.RequestException as e:
        print(f"发生错误: {e}")
        return None


def send_post_request(session, url, data, headers=None):
    try:
        # 发送 POST 请求
        response = session.post(url, data=data, headers=headers)

        # 检查请求是否成功
        response.raise_for_status()

        # 解决乱码
        response.encoding = 'utf-8'
        return response.text

        # # 尝试解析 JSON 响应
        # try:
        #     json_response = response.json()
        #     return json_response
        # except json.JSONDecodeError:
        #     # 如果响应不是 JSON 格式，返回文本内容
        #     return response.text

    except requests.RequestException as e:
        print(f"发生错误: {e}")
        return None


# 使用示例
'''
__VIEWSTATE: 7gH1CGr857gvKfh2vJZgnUffcsrQaFOoubyeWRvAU1rLxLxej6ejzvS1cR9/3gZ2qFq0Qr/jQ/TKhqeYi71jJNokqOD44UFNZ8U/PMp4GQP/ej8QIwPCm5o9DAbPgk2bb9Pjt3azPIlVCPjvCOtfO+3Ag2s=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://www.gushiwen.cn/user/collect.aspx
email: 11111111@qq.com
pwd: 123456
code: 1234
denglu: 登录
'''

# url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'
url = 'https://www.gushiwen.cn/user/login.aspx'

params = {
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    # 'Authorization': 'Bearer YOUR_TOKEN_HERE'  # 如果需要认证
}

response = send_get_request(url, params, headers)
# print("响应:", response)
# 解析
tree = etree.HTML(response)

# 获取元素
viewstate = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
viewstategenrator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
# print('__VIEWSTATE', viewstate)
# print('__VIEWSTATEGENERATOR', viewstategenrator)

# 获取验证码图片
code = tree.xpath('//img[@id="imgCode"]/@src')[0]
img_url = f'https://www.gushiwen.cn{code}'
# print('img_url', img_url)

# ===========图片请求要用登录请求共用session==============
session = requests.session()

# 图片保存路径
save_path = 'downloads/my_image.jpg'
download_image(session, img_url, save_path)

# 下载图片，获得对应的验证码
code_name = input('请输入你的验证码：')
# code_name = chaojiying.parse_pic_str(save_path)

# 登录url
login_url = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'

form_data = {
    '__VIEWSTATE': '',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': 'xxx@qq.com',
    'pwd': '123456',
    'code': code_name,
    'denglu': '登录'
}

response_post = send_post_request(session, login_url, form_data, headers)
print(response_post)
with open('gushiwen.html', 'w', encoding='utf-8') as file:
    file.write(response_post)

