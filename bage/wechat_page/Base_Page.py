#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 12:47
# @Author  : A one
import logging
import time
import allure
import yaml
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class DriverPage:
    """
    公共页面
    """
    # 全局参数
    _base_url = ""

    def __init__(self, base_driver: WebDriver=None):
        """
        :param base_driver:
        """
        if base_driver == None:
            # 初始化driver
            self.driver = webdriver.Chrome()
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(15)
            # cookies 植入driver
            f = yaml.safe_load(open("../../data/cookies.yml"))
            for cookies in f:
                self.driver.add_cookie(cookies)
            self.driver.get(self._base_url)
            time.sleep(2)
        else:
            self.driver = base_driver

    # 一：重新封装查找元素
    def find(self, by, locator=None):

        if locator == None:
            # 传入的元祖参数
            try:
                c = self.driver.find_element(*by)
            except Exception:
                logging.info('未找到元素：%s' % by[1])
        else:
            # 传入的2个参数by，locator
            try:
                c = self.driver.find_element(by=by,value=locator)
            except Exception:
                logging.info('未找到元素：%s' % locator)
        return c

    # 二：重新分钟查找元素
    def find_ele(self,loc):
        try:
            WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception:
            logging.info('未找到元素：%s' % loc[1])
            allure.attach(self.driver.get_screenshot_as_png(), "未找到元素",
                          allure.attachment_type.PNG)

    def find_eles(self, *loc):
        # 重写查找多个元素方法
        try:
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except AttributeError:
            # print('页面未找到元素')
            logging.error('未找到元素：%s 请检查！' % loc[1])
            screen_shot = self.get_screen()
            logging.error('已截图，路径：%s' % screen_shot)