#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/14 11:02
# @Author: KeyJia
# @File: def.py

def func1():
    """testing"""
    print('in the func1')
    return 0

def func2():
    print()
    print('in the func2')
    return 0

x = func1()
y = func2()

print('form func1 return is %s' %x)
print('form func2 return is %s' %x)