#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 11:25
# @Author  : A one

"""
driver界面

"""
from web_master.app.app_page.base_page import BasePage
from appium import webdriver
from web_master.app.app_page.main_page import Main


class App(BasePage):

    #   处事默认包名、启动activity
    _package = "com.tencent.wework"
    _activity = "com.github.moduth.blockcanary.ui.DisplayActivity"
    def start(self):
        #   driver 为空初始化
        if self._driver is None:
            engine = {}
            engine['platformName'] = "android"  # 设备类型
            engine['deviceName'] = "127.0.0.1:21503"    # 设备号
            engine['appPackage'] = self._package    # 包名
            engine['appActivity'] = self._activity
            engine['noReset'] = True    # 不停止应用程序，不清除应用数据，不卸载apk(反：fullReset)
            self._driver = webdriver.Remote("http：//localhost:4723/wd/hub", engine)
            self._driver.wait_activity(15)  # 隐式等待

        #   如果driver为空直接启动activity
        else:
            self._driver.start_activity(self._package,self._activity)

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:

        return Main(self._driver)






