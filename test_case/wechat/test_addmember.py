#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 15:01
# @Author  : A one
import allure
import pytest

from web_master.bage.wechat_page.Home_Page import HomePage


@allure.title("添加成功功能")
class TestAddMember:

    @allure.story("添加成员")
    def test_add_member(self):
        """
        1.跳转添加成员界面
        2.添加成员界面添加成员
        3.保存成员，返回通讯界面
        4.断言保存成功

        :return:
        """
        # 实例化
        home = HomePage()
        # 跳转成员界面
        list_iphone = home.goto_member().add_member(name="可",alias="可可",acctid="11111",iphone="13510586333").get_member()
        print(list_iphone)
        assert '13510586333' in list_iphone
