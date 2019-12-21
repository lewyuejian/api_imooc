#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: data_config.py
@time: 2019/12/20 10:26
@desc:
'''
class GlobalVar:
    #case_id
    Id = '0'
    url = '1'
    # 是否执行
    run = '2'
    # 请求方式
    request_way = '3'
    header = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    data = '8'
    # 预期结果
    expect = '9'
    result = '10'


def get_id():
    """
    获取Case_Id
    :return:
    """
    return GlobalVar.Id

def get_url():
    """
    获取请求地址
    :return:
    """
    return GlobalVar.url

def get_run():
    """
    是否执行
    :return:
    """
    return GlobalVar.run

def get_run_way():
    """
    获取请求方式
    :return:
    """
    return GlobalVar.request_way

def get_header():
    """
    获取请求头
    :return:
    """
    return GlobalVar.header

def get_case_depend():
    return GlobalVar.case_depend

def get_data_depend():
    """
    获取数据依赖
    :return:
    """
    return GlobalVar.data_depend

def get_field_depend():
    """
    数据依赖所属的字段
    :return:
    """
    return  GlobalVar.field_depend

def get_data():
    """
    获取请求数据
    :return:
    """
    return GlobalVar.data

def get_expect():
    """
    获取预期结果
    :return:
    """
    return GlobalVar.expect

def get_result():
    """
    获取实际结果
    :return:
    """
    return GlobalVar.result

def get_header_value():
    header = {
        "header":"1234",
        "cookie":"pophas"
    }