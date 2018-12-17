#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 14:12
# @Author: KeyJia
# @File: 高阶函数.py

def add(a,b,f):
    return f(a)+f(b)

res = add(3,-6,abs)
print(res)