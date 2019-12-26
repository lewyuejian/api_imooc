#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: run_test.py
@time: 2019/12/25 10:16
@desc:
'''
import sys
sys.path.append("F:/python/imooc")
from data.run_method import RunMethod
from data.get_data import GetData
from data.common_util import CommonUtil
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            expect = self.data.get_expcet_data(i)
            if is_run:
                res = self.run_method.run_main(method,url,data,header)
                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,'pass')
                    print("测试通过")
                else:
                    self.data.write_result(i, 'fail')
                    print("测试失败")
               # return res


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()




