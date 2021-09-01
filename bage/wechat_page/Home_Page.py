#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 19:36
# @Author  : A one
import time

from web_master.bage.wechat_page.Add_member_page import AddMember
from web_master.bage.wechat_page.Communication_Page import CommunicationPage
from web_master.bage.wechat_page.Base_Page import DriverPage
from selenium.webdriver.common.by import By


class HomePage(DriverPage):
    """
    首页
    """
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_member(self):
        """
        ：跳转成员界面
        ：添加成员
        :return: 目标页面
        """
        # 点击添成员，跳转添加成员界面
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item").click()
        time.sleep(3)
        return AddMember(self.driver)

    def goto_communication(self):
        """
        :return:
        """
        pass
        return CommunicationPage(self.driver)

    def Send_messages(self):
        """

        :return:
        """
        pass
        return

