#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 19:32
# @Author  : A one

import pytest
import logging

# 定义基本测试环境


@pytest.fixture(scope='module', autouse=True)
def start():
    logging.info("===初始化====")
    pass


# 关闭浏览器
@pytest.fixture(scope="session", autouse=True)
def demo_end():
    yield
    logging.info("demo this end ~~~")
    print("yield demo end !!!!")