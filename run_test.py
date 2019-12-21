#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: run_test.py
@time: 2019/12/19 9:57
@desc:
'''
import unittest,time
from test_unittest import TestMethod
import HTMLTestRunner

suite=unittest.TestSuite()
suite.addTest(TestMethod('test_01'))
suite.addTest(TestMethod('test_02'))
now=time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
filename='F:/python/imooc/report' + now + '_result.html'
print(filename)
with open(filename, 'wb') as fp:
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告',
                                         description=u'用例执行详情：')
    runner.run(suite)
# fp.close()
#  #unittest.TextTestRunner().run(suite)
