#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 18:57
# @Author  : A one
import pytest
import yaml


# yaml数据读取一：
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


def test_getdatas_byfixture(get_datas_byfixture):
    print(get_datas_byfixture)


# yml 数据读取二
def get_yaml():

    test_data = yaml.safe_load(open("../data/add.yml"))
    print(test_data['three'])
    return test_data