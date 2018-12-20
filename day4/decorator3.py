#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 15:03
# @Author: KeyJia
# @File: decorator3.py

x = 0
def grandpa():
    x =1
    def dad():
        x=2
        def son():
            x=3
            print(x)
        son()
    dad()
grandpa()
