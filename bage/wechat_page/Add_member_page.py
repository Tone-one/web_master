#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 11:37
# @Author  : A one
import time

from selenium.webdriver.common.by import By
from web_master.bage.wechat_page.Base_Page import DriverPage
from web_master.bage.wechat_page.Communication_Page import CommunicationPage


class AddMember(DriverPage):
    """
    添加成员界面
    """
    _username_locator = (By.ID, 'username')

    _base_url = ""
    def add_member(self,name,alias,acctid,iphone):
        """
        1.添加成员:
            →输入姓名
            →输入别名
            →输入账号
            →输入手机号
            →保存
        2.保存自动返回通讯录界面
        :return:
        """
        # 需要导入WebDriver 注释，否则不会自动关联
        self.find(self._username_locator).send_keys(name)
        time.sleep(2)
        self.find(By.CSS_SELECTOR,"#memberAdd_english_name").send_keys(alias)
        time.sleep(2)
        self.find(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys(acctid)
        time.sleep(2)
        self.find(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(iphone)
        time.sleep(2)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        time.sleep(3)
        return CommunicationPage(self.driver)

    def add_member_fail(self):
        """
        输入
        :return:
        """
        pass

