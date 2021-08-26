#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 19:08
# @Author  : A one
import logging

import allure

from web_master.bage.baidu_page import BaiduPage
from time import sleep
import pytest


@allure.feature("百度搜索")
@pytest.mark.run(order=4)
class TestBaidu:

    def test_baidu_01(self,browser,base_url):
        """
        名称：百度搜索"pytest"
        步骤：
        1、打开浏览器
        2、输入"pytest"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        logging.info("开始执行百度搜索")
        with allure.step("浏览器启动"):
            page = BaiduPage(browser)
            page.get(base_url)
            allure.attach(browser.get_screenshot_as_png(), "截图测试", allure.attachment_type.PNG)
        logging.info("搜索A one")
        with allure.step("A one"):
            page.search_input = "A one"
            page.search_button.click()
        sleep(2)
        assert browser.title == "A one_百度搜索"

