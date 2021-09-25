#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 11:25
# @Author  : A one

"""
driver界面

"""
from web_master.bage.app_page.base_page import BasePage


class App(BasePage):

    def start(self):

        if self._driver is None:
            engine = {}
            engine['platformName'] = "android"  # 设备类型
            engine['deviceName'] = "android"    # 设备号
            engine['appPackage'] = "android"    # 包名
            engine['appActivity'] = "android"
            engine['noReset'] = True    # 不停止应用程序，不清除应用数据，不卸载apk(反：fullReset)


