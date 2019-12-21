#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: operation_json.py
@time: 2019/12/20 9:52
@desc:
'''
import json

class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        """
        读取json文件
        :return:
        """
        with open('../dataconfig/login.json') as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        """
        根据关键字获取数据
        :return:
        """
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('login'))
