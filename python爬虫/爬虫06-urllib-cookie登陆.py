# 适用的场景：数据采集的时候 需要绕过登陆 然后进入到某个页面
# 个人信息页面是utf-8  但是还报错了编码错误  因为并没有进入到个人信息页面 而是跳转到了登陆页面
# 那么登陆页面不是utf-8  所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够  所以访问不成功
import urllib.request
import urllib.parse
import json


def create_request():
    url = 'https://www.gulixueyuan.com/my/courses/learning'
    # UA反爬
    headers = {
        'cookie': '_ga=GA1.1.1285008252.1710553949; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOWhiVFU1Y25JMGVETkFaV1IxYzI5b2J5NXVaWFE9OjE3NDIwOTExNzk6NmM0NjkyNGUwY2FmYTRhMDA0ZjlkNWNjYjgyYzU3ZmI1ZGUyNTYzOGY2YjFlYmI0ZTJhNTViNWMwNTM5MjhjMQ%3D%3D; PHPSESSID=9rlvqhp7csqrj2nebcee8gvmr0; online-uuid=BE2904B0-5D36-F17B-19C3-43A411C981F7; __gads=ID=9a2aeaf469a448ac:T=1715612397:RT=1722741351:S=ALNI_MYRdGzXC2VX1kh2NjbyJEJ9xvdT5A; __gpi=UID=00000e1a7ec18812:T=1715612397:RT=1722741351:S=ALNI_MZp6N-U5yGJ_vDi6PHRHAFBwkDvnA; __eoi=ID=30a1db1ed243fbce:T=1715612397:RT=1722741351:S=AA-AfjY5MW8ceu72VLNPja9zmtGG; _ga_F7LSTV2E7L=GS1.1.1722744503.17.1.1722744633.0.0.0',
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    req_data = None

    # 请求对象定制
    return urllib.request.Request(url, req_data, headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(json.loads(content))
    return content


def down_load(content):
    with open('guli.html', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    # 请求对象的定制
    request = create_request()
    # 获取网页源码
    content = get_content(request)
    # 下载
    down_load(content)
