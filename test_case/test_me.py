#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 17:05
# @Author  : A one

import pytest
import yaml
import logging
import allure
# from web_master.bage.Readdata import get_datas_byfixture

def get_yaml_add():
    with open("../data/add.yml") as f:
        yaml_data = yaml.safe_load(f)
    get_yaml_two= yaml_data.get("three")
    get_yaml_three = yaml_data.get("ids")
    return get_yaml_two, get_yaml_three


@pytest.fixture(params=get_yaml_add()[0],ids=get_yaml_add()[1])
def get_datas_byfixture(request):
    print(f"request.param == {request.param}")
    return request.param

@allure.feature("加法")
class TestWeb:

    @allure.story("两数之和")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("information",yaml.safe_load(open("../data/add_1.yml")))
    def test_add(self,information):
        logging.info("add -1")
        add_sum = sum(information)
        print(add_sum)
        return add_sum


    @allure.story("连续3个+")
    @pytest.mark.run(order=1)
    @pytest.param()
    def test_add_01(self):
        logging.info("add -2")
        add_sum = sum([get_datas_byfixture()[0],get_datas_byfixture()[1],get_datas_byfixture()[2]])
        return add_sum

    def test_getdatas_byfixture(self,get_datas_byfixture):
        p = get_datas_byfixture
        print(p[0])
