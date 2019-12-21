#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: run_method.py
@time: 2019/12/20 12:08
@desc:
'''
import requests
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            requests.post(url=url,data=data,headers=header).json()
        else:
            requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data,header):
        res=None
        if header != None:
            requests.get(url=url, data=data, headers=header).json()
        else:
            requests.get(url=url, data=data).json()
        return res

    def run_main(self,method,url,data,header):
        pass