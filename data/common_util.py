#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: common_util.py
@time: 2019/12/25 14:10
@desc:
'''
class CommonUtil:
    def is_contain(self,str_one,str_two):
        """
        判断一个字符串是否在另一个字符串中
        :param str_one: 查找的字符串
        :param str_two:被查找的字符串
        :return:
        """
        flag = None
        if isinstance(str_one,str):
            str_one = str_one.encode('unicode-escape').decode('unicode-escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag