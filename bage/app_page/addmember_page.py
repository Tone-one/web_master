# __author:A one
# data:2021/9/29 0029
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:
    _driver: WebDriver

    def __init__(self, driver):
        self._driver = driver

    #   1、选择手动添加成员
    #   2、输入姓名
    #   3、输入手机号
    #   4、保存添加

    def add_member(self, iphone, name):
        self._driver.find_element()
        return
