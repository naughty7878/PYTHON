import urllib.request
import random


def atest01():
    url = 'https://cip.cc'

    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)

    proxies = {
        'https': '117.42.94.138:18003'
    }
    # handler  build_opener  open
    handler = urllib.request.ProxyHandler(proxies=proxies)

    opener = urllib.request.build_opener(handler)

    response = opener.open(request)

    content = response.read().decode('utf-8')

    with open('daili.html', 'w', encoding='utf-8') as f:
        f.write(content)


def atest02():
    url = 'https://cip.cc'

    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)

    proxies_pool = [
        {'http': '118.24.219.151:16817'},
        {'http': '118.24.219.151:16817'}
    ]

    proxies = random.choice(proxies_pool)

    # handler  build_opener  open
    handler = urllib.request.ProxyHandler(proxies=proxies)

    opener = urllib.request.build_opener(handler)

    response = opener.open(request)

    content = response.read().decode('utf-8')

    with open('daili.html', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    atest01()
