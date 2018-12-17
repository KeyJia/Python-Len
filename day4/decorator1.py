#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 15:03
# @Author: KeyJia
# @File: decorator.py


#
# def foo():
#     print('in the foo')
# foo()



def foo():
    print('in the foo')
    bar()

def bar():
    print('in the bar')

foo()


calc = lambda x:x*3
print(calc(3))