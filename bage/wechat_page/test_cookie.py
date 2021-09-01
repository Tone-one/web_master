#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 9:33
# @Author  : A one
import time

import yaml
from selenium import webdriver
from web_master.bage.wechat_page.Base_Page import DriverPage

class TestGetCookies():

    def setup_class(self):

        self.driver = webdriver.Chrome()

    def test_cookies_data(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 等待扫码登录
        time.sleep(15)
        """
        :登录成功后，获取cookies
        :将cookies写入到本地yaml文件
        """
        cookies = self.driver.get_cookies()
        with open("../../data/cookies.yml", "w") as f:
            yaml.safe_dump(cookies, f)

    def test_cookies_add(self):
        """
        打开页面
        植入cookies
        重新打开页面刷新
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 打开文件，获取yml文件数据
        time.sleep(1)
        with open("../../data/cookies.yml") as f:
            cookies_yaml = yaml.safe_load(f)
        # 遍历获取的数据，提前cookie，并植入driver
        for cookie in cookies_yaml:
            self.driver.add_cookie(cookie)
            print(cookie)
        time.sleep(2)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

