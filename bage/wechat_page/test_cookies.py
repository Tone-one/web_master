#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 11:14
# @Author  : A one
# import time
# import yaml
# from selenium import webdriver
#
#
# class TestCookieLogin:
#     def setup_class(self):
#         self.driver = webdriver.Chrome()
#     def test_get_cookie(self):
#         self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
#         time.sleep(20)
#         cookies = self.driver.get_cookies()
#         with open("../../test_case/wechat/cookies.yaml", "w") as f:
#             yaml.safe_dump(cookies, f)
#     def test_add_cookie(self):
#         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#         with open("../../test_case/wechat/cookies.yaml") as f:
#             cookies = yaml.safe_load(f)
#         for cookie in cookies:
#             self.driver.add_cookie(cookie)
#         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")