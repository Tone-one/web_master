#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 14:36
# @Author  : A one
import pytest
import os

if __name__ == '__main__':
    pytest.main(["-sq",
                 "--alluredir", "./allure-results"])
    os.system(r"allure generate ./result -o ./report")

"""
====
pip3 install pytest-rerunfailures  重跑失败用例插件
Powershot 执行：
pytest -sq xx.py - -reruns 5 - -reruns - delay 2  
重跑5次   每次重跑延迟2秒
====
1.参数：-s
运行过程中执行print打印函数
2.参数：-v 或 -q
打印用例执行的详细 -v/简略过程 -q
3.运行指定的函数（使用两对冒号 : :分隔）
pytest 模块名::类名::函数名 
4.pytest -m ”标记“
执行特定的测试用例
"""
"""
pytest -s --alluredir=./result
allure generate ./result -o ./report
"""