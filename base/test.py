#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: test.py
@time: 2019/12/18 14:40
@desc:
'''
import requests
import json
class RunMain:
    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)
    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return json.loads(res)
if __name__ == '__main__':

    url = 'http://47.106.25.58:8019/login/login.json?'
    data = {
        'userName':'account',
        'password':'123',
    }
    run = RunMain()
    print(run.run_main(url,'POST',data))


