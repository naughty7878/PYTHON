from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print("ChromeDriver 和 Chrome 浏览器兼容性验证成功！")
driver.quit()