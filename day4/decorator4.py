#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/18 11:00
# @Author: KeyJia
# @File: decorator4.py

import time
def timer(func):
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco()

@timer
def test1():
    time.sleep(3)
    print('in the test1')

@timer
def test2():
    time.sleep(3)
    print('in the test2')

test1
test2

