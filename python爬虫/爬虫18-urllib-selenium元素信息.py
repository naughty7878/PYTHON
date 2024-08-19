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

# ================元素信息=========================

# 根据id来找到对象
search_button = browser.find_element(by=By.ID, value='su')
print(search_button)
# 获取属性值
print(search_button.get_attribute('class'))
# 获取元素标签名字
print(search_button.tag_name)

link_button = browser.find_element(by=By.LINK_TEXT, value='贴吧')
print(link_button)
# 获取标签之间的内容
print(link_button.text)







# 获取网页源码
# content = browser.page_source
# print(content)

# 完成操作后记得关闭浏览器
# browser.quit()
