#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 11:57
# @Author  : A one
from selenium.webdriver.common.by import By

from web_master.bage.wechat_page.Base_Page import DriverPage


class CommunicationPage(DriverPage):
    """
    通讯记录界面
    """
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts" # 调试
    def get_member(self):

        member_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(5)')
        phone_list = []
        for ele in member_list:
            phone_list.append(ele.text)
        return phone_list

    def delete_member(self):
        pass
        return


if __name__ == "__main__":

    a = CommunicationPage()
    a.get_member()