#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 17:34
# @Author  : A one
# 封装

# 2数之和
import logging
import math


def add_2(a, b):
    add_sum = a/b
    print(add_sum)
    return add_sum

# 3数之和
def add_3(a, b, c):
    add_sum = a + b + c
    return add_sum

if __name__ == "__main__":
    add_2(math.pi,2)
