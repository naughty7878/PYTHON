import time

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

# 休眠2秒
time.sleep(2)

# ================元素交互=========================
# 在搜索框中输入内容
input_search = browser.find_element(by=By.NAME, value='wd')
input_search.send_keys('周杰伦')

# 找到并点击搜索按钮
search_button = browser.find_element(by=By.ID, value='su')
search_button.click()

# 等待搜索结果加载（使用显式等待）
wait = WebDriverWait(browser, 10)
next = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="n"]')))

# 保存整个页面的截图
browser.save_screenshot('screenshot.png')

# 滚动到页面底部
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 平滑滚动到底部
browser.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")

# 休眠2秒
time.sleep(2)
# 点击下一页
next.click()


# 休眠2秒
time.sleep(2)
# 浏览器后退
browser.back()


# 休眠2秒
time.sleep(2)
# 浏览器前进
browser.forward()

# 休眠2秒
time.sleep(3)


# 完成操作后记得关闭浏览器
browser.quit()
