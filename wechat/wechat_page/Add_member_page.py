#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 11:37
# @Author  : A one
import time

import allure
from selenium.webdriver.common.by import By
from web_master.wechat.wechat_page.Base_Page import DriverPage


@allure.feature("添加成员功能")
class AddMember(DriverPage):
    """
    添加成员界面
    """
    _username_locator = (By.ID, 'username')
    _base_url = ""
    @allure.story("成功添加成员")
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

        with allure.step("# 姓名输入"):
            self.find(self._username_locator).send_keys(name)
        with allure.step("# 别名输入"):
            time.sleep(2)
            self.find(By.CSS_SELECTOR,"#memberAdd_english_name").send_keys(alias)
            time.sleep(2)
        with allure.step("# 账号输入"):
            self.find(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys(acctid)
            time.sleep(2)
        with allure.step("# 手机号输入"):
            self.find(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(iphone)
            time.sleep(2)
        with allure.step("# 保存添加"):
            self.find(By.CSS_SELECTOR,".js_btn_save").click()
            time.sleep(3)
        from web_master.wechat.wechat_page.Communication_Page import CommunicationPage # 方法内导入，避免双向导入问题
        return CommunicationPage(self.driver)  # 指向通讯录界面

    @allure.story("手机号已存在添加成员失败")
    def add_member_fail(self):
        """
        1.进入通讯录界面
        2.添加成员
        3.输入已存在的手机号
        4.获取断言手机号已经存在
        :return:
        """
        pass
        return

