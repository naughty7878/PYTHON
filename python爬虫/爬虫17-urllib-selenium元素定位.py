# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
url = 'https://www.baidu.com/'
browser.get(url)

# 元素定位

# 根据id来找到对象
search_button = browser.find_element(by=By.ID, value='su')
print(search_button)
# 根据name来找到对象
input_search = browser.find_element(by=By.NAME, value='wd')
print(input_search)
# find_element 返回单个值
# find_elements 返回列表, XPATH 表示根据xpath语句来获取对象
# search_button2 = browser.find_elements(by=By.XPATH, value='//input[@id="su"]')
# print(search_button2)
# input_labels = browser.find_elements(by=By.TAG_NAME, value='input')
# print(input_labels)
# CSS_SELECTOR 表示根据CSS选择器来获取对象
# search_button3 = browser.find_elements(by=By.CSS_SELECTOR, value='#su')
# print(search_button3)
# 根据连接对象获取对象
# link_button = browser.find_element(by=By.LINK_TEXT, value='贴吧')
# print(link_button)

# 获取网页源码
# content = browser.page_source
# print(content)

# 完成操作后记得关闭浏览器
# browser.quit()
