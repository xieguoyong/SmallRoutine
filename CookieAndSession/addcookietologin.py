from selenium import webdriver
from selenium.webdriver.common.by import By
from CookieAndSession.handle_data import get_yaml


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.baidu.com")
# 添加Cookie
driver.add_cookie({'name': 'BAIDUID', 'value': get_yaml()['BAIDUID']})
driver.add_cookie({'name': 'BDUSS', 'value': get_yaml()['BDUSS']})
driver.refresh()

# 获取登录用户名并打印
username = driver.find_element(By.CLASS_NAME, "user-name").text
print(username)

driver.quit()
