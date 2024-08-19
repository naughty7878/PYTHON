import time

# 导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 设置 本地浏览器 路径
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# 浏览器选项
chrome_options = webdriver.ChromeOptions()
# 设置 Chrome 选项
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 硬件加速
# 保持浏览器打开
chrome_options.add_experimental_option("detach", True)
# 设置 Chrome 二进制文件位置
chrome_options.binary_location = chrome_path

# 创建浏览器操作对象
browser = webdriver.Chrome(options=chrome_options)

# 访问网站
url = 'https://www.baidu.com/'
browser.get(url)

# 休眠2秒
time.sleep(2)
print(f"当前页面标题: {browser.title}")
# 保存整个页面的截图
browser.save_screenshot('screenshot1.png')

# ================元素交互=========================
# 在搜索框中输入内容
input_search = browser.find_element(by=By.NAME, value='wd')
input_search.send_keys('周杰伦')

# 找到并点击搜索按钮
search_button = browser.find_element(by=By.ID, value='su')
search_button.click()

# 等待搜索结果加载（使用显式等待）
wait = WebDriverWait(browser, 2)
next = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="n"]')))

# 保存整个页面的截图
browser.save_screenshot('screenshot2.png')

# 完成操作后记得关闭浏览器
browser.quit()
