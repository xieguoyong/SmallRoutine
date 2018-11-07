import unittest
from selenium import webdriver
from .handle_data import get_yaml
import time

# 从yaml获取浏览器
browser = get_yaml()['browser']
# 从yaml获取url
url = get_yaml()['url']


class MyUnit(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # 启动浏览器
        if browser == 'ie':
            driver = webdriver.Ie()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            print("brower value error")

        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get(url)

        # 从yaml中获取用户信息并写入sessionStorage，实现免登录
        driver.execute_script('sessionStorage.setItem("access_token", arguments[0]);', get_yaml()['access_token'])
        driver.execute_script('sessionStorage.setItem("userName", arguments[0]);', get_yaml()['userName'])
        driver.execute_script('sessionStorage.setItem("userId", arguments[0]);', get_yaml()['userId'])
        driver.execute_script('sessionStorage.setItem("roleName", arguments[0]);', get_yaml()['roleName'])
        driver.get(url + '/slide')
        driver.refresh()
        time.sleep(30)

    def test(self):
        pass

    @classmethod
    def tearDown(cls):
        pass


if __name__ == '__main__':
    x = MyUnit()
