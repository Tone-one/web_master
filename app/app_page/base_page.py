# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 0025 15:43
# @Author  : A one
# @FileName: base_page.py
# @Software: PyCharm

from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 公共方法的封装
    def find(self, locator, value: str = None):
        # 如果传的是元组，只需使用一个参数locator
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)
