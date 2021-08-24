#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 18:01
# @Author  : A one
import yaml


def test_yaml():

    test_data = yaml.safe_load(open("../data/add.yml"))
    print(test_data['three'])
    return test_data

