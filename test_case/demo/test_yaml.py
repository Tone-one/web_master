#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 18:01
# @Author  : A one
import logging

import allure
import pytest
import yaml


@allure.feature("Yaml 测试")
@pytest.mark.run(order=3)
def test_yaml():

    test_data = yaml.safe_load(open("./data/add.yml"))
    logging.info("======test_yaml========")
    return test_data


@allure.feature("Yaml 测试_1")
@pytest.mark.run(order=3)
def test_yaml_1():

    test_data = yaml.safe_load(open("./data/add.yml"))
    logging.info("======test_yaml========")
    return test_data
