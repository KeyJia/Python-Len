#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/14 16:57
# @Author: KeyJia
# @File: func.test5.py

# def test(x,y):
#     print(x)
#     print(y)
# test(1,3)
#
#
#
# def test2(**kwargs):
#     print(kwargs)
#
# test2(name='keyjia',age=20,sex='M')


#
# def test3(name,**kwargs):
#     print(name)
#     print(kwargs)
#
# test3(name='key',age=18,sex=8)

##**kwargs: 按收n个关键字参数，转换成字典的方式

def test4(name,age=19,*args,**kwargs):
    print(name)
    print(age)
    print(kwargs)
    logger("TEST4")

def logger(source):
    print("from %s" % source)

test4('keyj',age=32,sex='M',hobby='tesla')


