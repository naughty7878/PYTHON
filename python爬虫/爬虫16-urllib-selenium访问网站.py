import urllib.request
# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# url = 'https://www.jd.com'
#
# headers = {
#     'user-agent':
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
# }
#
# request = urllib.request.Request(url=url, headers=headers)
#
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# print(content)


# 设置 ChromeDriver 路径
path = 'chromedriver.exe'
service = Service(path)

# 浏览器选项
chrome_options = webdriver.ChromeOptions()
# 保持浏览器打开
chrome_options.add_experimental_option("detach", True)

# 创建浏览器操作对象
browser = webdriver.Chrome(service=service, options=chrome_options)

# 访问网站
url = 'https://www.jd.com/'
browser.get(url)

# 获取网页源码
content = browser.page_source
print(content)

# 完成操作后记得关闭浏览器
# browser.quit()