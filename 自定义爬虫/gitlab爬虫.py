import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def scrape_projects():
    """
    爬取项目列表并将数据实时写入 projects.json 文件
    """
    try:
        # 打开 JSON 文件，准备写入数据
        with open("projects.json", "w", encoding="utf-8") as f:
            # 写入文件的开头（JSON 数组的开头）
            f.write("[\n")

            # 第一步：打开登录页并登录
            driver.get("http://git.com/users/sign_in")  # 替换为实际的登录页 URL
            print("已打开登录页")

            # 输入用户名和密码
            username_input = driver.find_element(By.ID, 'user_login')  # 替换为实际的用户名输入框属性
            password_input = driver.find_element(By.NAME, "user[password]")  # 替换为实际的密码输入框属性
            username_input.send_keys("xx@qqcom")  # 替换为你的用户名
            password_input.send_keys("123")  # 替换为你的密码

            # 点击登录按钮
            login_button = driver.find_element(By.NAME, "commit")  # 替换为实际的登录按钮选择器
            login_button.click()
            print("已登录")

            # 等待登录完成并跳转到列表页
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="projects-list"]')))
            print("已进入列表页")

            # 第二步：循环处理列表页
            first_item = True  # 标记是否是第一个项目，用于处理 JSON 数组的逗号
            while True:
                # 获取列表项
                items = driver.find_elements(By.XPATH, '//ul[@class="projects-list"]/li')  # 替换为实际的列表项选择器
                print(f"当前页共有 {len(items)} 个列表项")
                if len(items) == 0:
                    break

                # 遍历列表项
                for index, item in enumerate(items):
                    # 获取信息
                    item_namespace_name = item.find_element(By.CSS_SELECTOR, ".namespace-name").text  # 替换为实际的标题
                    item_namespace_name = re.sub(r'\s*/\s*', '/', item_namespace_name.strip())

                    item_project_name = item.find_element(By.CSS_SELECTOR, ".project-name").text
                    item_project_name = re.sub(r'\s*/\s*', '/', item_project_name.strip())

                    # 查找描述元素
                    item_describes = item.find_elements(By.XPATH,
                                                        './/div[@class="project-details"]/div[contains(@class, "description")]/p')
                    item_describe = item_describes[0].text if len(item_describes) > 0 else ''

                    # 提取用户角色
                    item_user_roles = item.find_elements(By.XPATH,
                                                         './/div[@class="project-details"]//span[@class="user-access-role"]')
                    item_user_role = item_user_roles[0].text if len(item_user_roles) > 0 else ''
                    print(
                        f'item_namespace_name = {item_namespace_name}, item_project_name = {item_project_name}, item_describe = {item_describe}, item_user_role = {item_user_role}')

                    # 判断用户角色
                    if item_user_role == 'Guest':
                        print(f"跳过 Guest 权限的项目: {item_namespace_name}/{item_project_name}")
                        continue

                    # 点击列表项进入详情页
                    detail_btn = item.find_element(By.XPATH, './/div[@class="project-details"]/h3[contains(@class, "prepend-top-0")]/a[@class="text-plain"]')
                    detail_btn.click()
                    print(f"已点击第 {index + 1} 个列表项")

                    # 等待详情页加载
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, '//div[@class="project-clone-holder"]')))  # 替换为实际的详情内容选择器

                    # 获取详情信息
                    detail_http = driver.find_element(
                        By.XPATH,
                        '//div[contains(@class, "container-fluid")]//div[@class="project-clone-holder"]//a[contains(@class, "http-selector")]'
                    ).get_attribute("href")

                    detail_ssh = driver.find_element(
                        By.XPATH,
                        '//div[contains(@class, "container-fluid")]//div[@class="project-clone-holder"]//a[contains(@class, "ssh-selector")]'
                    ).get_attribute("href")
                    print(f'detail_ssh = {detail_ssh}, detail_http = {detail_http}')

                    # 将数据存储为字典
                    project = {
                        "item_namespace_name": item_namespace_name,
                        "item_project_name": item_project_name,
                        "item_describe": item_describe,
                        "item_ssh": detail_ssh,
                        "item_http": detail_http
                    }

                    # 将数据写入 JSON 文件
                    if not first_item:
                        f.write(",\n")  # 如果不是第一个项目，写入逗号分隔符
                    json.dump(project, f, ensure_ascii=False, indent=4)
                    first_item = False  # 标记第一个项目已处理

                    print("-" * 50)

                    # 返回列表页
                    driver.back()
                    print("已返回列表页")

                    # 等待列表页重新加载
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="projects-list"]')))

                # 第三步：点击下一页
                try:
                    next_button = driver.find_element(By.XPATH,
                                                     '//ul[contains(@class, "pagination")]/li[contains(@class, "next")]')  # 替换为实际的下一页按钮选择器
                    if "disabled" in next_button.get_attribute("class"):  # 检查下一页按钮是否禁用
                        print("已是最后一页，爬取结束")
                        break
                    next_link = next_button.find_element(By.XPATH, './/a')
                    next_link.click()
                    print("已点击下一页")

                    # 等待下一页加载
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="projects-list"]')))

                except Exception as e:
                    print("未找到下一页按钮或翻页失败，爬取结束")
                    break

            # 写入文件的结尾（JSON 数组的结尾）
            f.write("\n]")

    except Exception as e:
        print(f"爬取过程中出错: {e}")


if __name__ == '__main__':  # python程序主入口
    # 设置 ChromeDriver 路径
    # 下载地址：https://googlechromelabs.github.io/chrome-for-testing/#stable
    chrome_driver_path = "chromedriver.exe"  # 替换为你的 ChromeDriver 路径
    service = Service(executable_path=chrome_driver_path)

    # 初始化 Chrome 浏览器
    driver = webdriver.Chrome(service=service)

    # 调用爬虫方法
    scrape_projects()

    # 关闭浏览器
    driver.quit()
    print("程序结束")