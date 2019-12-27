#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: urls.py
@time: 2019/12/27 17:28
@desc:
'''


from django.urls import path
from web.views import Login
from web.terminalCheck import terminalcheck

urlpatterns = [
    path('',Login),
    path('home/',terminalcheck)
]
