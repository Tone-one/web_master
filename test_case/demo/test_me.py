#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 17:05
# @Author  : A one
import logging
import math

import pytest
import logging
import allure
from web_master.bage.Method import add_2
from web_master.bage.Readdata import get_datas_byfixture
from web_master.bage.Readdata import get_yaml_division

@pytest.mark.run(order=1)
@allure.issue("http:www.baidu.com")
@allure.feature("简单加法")
class TestAdd:
    # +
    @allure.story("连续3个+")
    def test_add_01(self,get_datas_byfixture,start):
        add_sum = sum(
            [get_datas_byfixture[0],
             get_datas_byfixture[1],
             get_datas_byfixture[2]]
        )
        logging.info("=add_01=")
        assert str(add_sum) == get_datas_byfixture[3]

    @allure.story("π")
    def test_add_02(self):
        i = math.pi
        add_sum = add_2(i,3)
        logging.info("=====add_02======")
        return add_sum == 1.0471975511965976
# 除法
@pytest.mark.add    # 标签
@pytest.mark.run(order=2)   # 用例执行顺序
@allure.description("这只是一个详细的说明")
@allure.feature("简单除法")
class TestDivision:

    @pytest.mark.parametrize(("a", "b","c"), get_yaml_division()['Division'], ids=get_yaml_division()['idsdiv'])
    def test_division_01(self, a, b, c,start):
        logging.info("=====division_01======")
        try:
            add_sum = add_2(a, b)
        except ZeroDivisionError as e:
            print(e)
            return False
        else:
            assert str(add_sum) == c
            return True


if __name__ == "__main__":
    pytest.main(["-s"])