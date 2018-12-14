#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/14 16:06
# @Author: KeyJia
# @File: func_test.py

import time

def looger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write('end action \n' %time_current)

def test1():
    print('in the test1')

    print('test end')


def test2():
    print('in the test2')


def test3():
    print('in the test3')

