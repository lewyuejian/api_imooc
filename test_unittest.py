#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: test_unittest.py
@time: 2019/12/18 15:43
@desc:
'''
import unittest,json,os,time
from base.test import RunMain
import HTMLTestRunner
from mock import *


print("/report/html_report.html")
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run=RunMain()

    def test_01(self):
        url='http://47.106.25.58:8019/login/login.json?'
        data={
            'userName': 'account',
            'password': '123',
        }

        res = self.run.run_main(url,'POST',data)

        #print(res)
        self.assertEqual(res['obj']['customCode'],'account',"测试失败")

    #@unittest.skip('test_02')
    def test_02(self):
        url='http://47.106.25.58:8019/login/login.json?'
        data={
            'userName': 'test',
            'password': '123',
        }

        res = self.run.run_main(url,'POST',data)
        self.assertEqual(res['obj']['customCode'],'test',"测试失败")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    now=time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename='F:/python/imoction/report' + now + '_result.html'
    print(filename)
    with open(filename,'wb') as fp:

        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告', description=u'用例执行详情：')
        runner.run(suite)
    #fp.close()
   #  #unittest.TextTestRunner().run(suite)
