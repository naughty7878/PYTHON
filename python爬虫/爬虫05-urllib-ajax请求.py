import urllib.request
import urllib.parse
import json

'''
# 1页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 深圳
# pid:
# pageIndex: 1
# pageSize: 10


# 2页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 深圳
# pid:
# pageIndex: 2
# pageSize: 10
'''


def create_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    # UA反爬
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    data = {
        'cname': '深圳',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    req_data = urllib.parse.urlencode(data).encode('utf-8')

    # 请求对象定制
    return urllib.request.Request(url, req_data, headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(json.loads(content))
    return content


def down_load(page, content):
    with open(f'kfc_{page}.json', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(page, content)
