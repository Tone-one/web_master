#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 11:57
# @Author  : A one
import time

from selenium.webdriver.common.by import By

from web_master.bage.wechat_page.Base_Page import DriverPage
from web_master.bage.wechat_page.Add_member_page import AddMember

class CommunicationPage(DriverPage):
    """
    通讯记录界面
    """

    # 调试
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def get_member(self):
        # 获取成员列表的手机号
        member_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        # 定义一个列表
        phone_list = []
        # 读取数据到ele
        for ele in member_list:
            phone_list.append(ele.text)     # 获取ele文本数据
            print(phone_list)
        return phone_list

    def goto_add_member_interface(self):
        """
        1.切换至通讯录界面
        2.添加添加按钮
        3.返回添加成员界面类
        :return:
        """
        # 切换至通讯录界面
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        # 点击添加成员
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar a:nth-child(2)").click()

        return AddMember(self.driver)  # 指向添加成员的界面


if __name__ == "__main__":

    a = CommunicationPage()
    a.goto_add_member_interface()

