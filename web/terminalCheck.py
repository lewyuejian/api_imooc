#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: terminalCheck.py
@time: 2019/12/27 17:34
@desc:
'''
from django.shortcuts import render
from django.http.response import HttpResponse

def terminalcheck(request):
    return render(request,'home.html',locals())
