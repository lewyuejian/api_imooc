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
import json
import requests
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            #print(res.status_code)
        return res.json()

    def get_main(self,url,data=None,header=None):
        res=None
        if header != None:
            res = requests.get(url=url, data=data, headers=header,verify=False).json()
        else:
           res = requests.get(url=url, data=data,verify=False).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)  # sort_keys排序 indent空格
