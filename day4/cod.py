#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 14:44
# @Author: KeyJia
# @File: cod.py

#装饰器，
#定义 - 本质是函数，（装饰其他函数）就是为其他函数添加附加功能
#原则 -
# 1,不能修改被装饰的函数的源代码
# 2，不有修改被装饰的函数的调用方式

# 实现装饰器的知识储备：
#1，函数即 “变量”
#2，高阶函数
# a,把一个函数名当做实参传给别外一个函数(在不修改被装饰函数源代码的情况下为其添加功能)
# b,返回值中包含函数名

#3，嵌套函数


#


def logger():
    print('logging')

def test1():
    pass
    logger()

def test2():
    pass
    logger()

test1()
test2()




