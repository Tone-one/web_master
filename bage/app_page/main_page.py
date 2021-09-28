#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 9:49
# @Author  : A one

#   首页
from web_master.bage.app_page.base_page import BasePage


class Main(BasePage):

    #   进入消息页面
    def goto_message(self):
        pass

    #   进入日程界面
    def goto_schedule(self):
        pass

    #   进入文档界面
    def goto_document(self):
        pass

    #   进入团队界面
    def goto_team(self):

        # 进入添加成员界面
        return AddMember(self._driver)
