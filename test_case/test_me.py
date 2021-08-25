#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 17:05
# @Author  : A one

import pytest
import logging
import allure
import yaml
from web_master.bage.Method import add_2
# yaml数据读取一：
def get_yaml_add():
    with open("../data/add.yml") as f:
        yaml_data = yaml.safe_load(f)
    get_yaml_two = yaml_data.get("three")
    get_yaml_three = yaml_data.get("ids")
    return (get_yaml_two, get_yaml_three)


@pytest.fixture(params=get_yaml_add()[0],ids=get_yaml_add()[1])
def get_datas_byfixture(request):
    print(f"request.param == {request.param}")
    return request.param


def test_getdatas_byfixture(get_datas_byfixture):
    print(get_datas_byfixture[0])


@allure.feature("计算器")
class TestAdd:
    # +
    @allure.story("连续3个+")
    @pytest.mark.run(order=1)
    def test_add_01(self,get_datas_byfixture):
        add_sum = sum(
            [get_datas_byfixture[0],
             get_datas_byfixture[1],
             get_datas_byfixture[2]]
        )
        logging.info(get_datas_byfixture[3])
        assert add_sum == get_datas_byfixture[3]

# 除法
@allure.feature("除法")
class TestDivision:

    @pytest.mark.parametrize("a,b",([1,2],[0.1,5],[-0.3,-0.1],[-0.1,2],[1,0]),
                             )
    def test_add_02(self,a,b):
        add_sum = add_2(a,b)
        print(add_sum)
        assert add_sum