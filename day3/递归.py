#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 13:44
# @Author: KeyJia
# @File: 递归.py

##递归有一个明确的结束条件
##每次进入更深入一层递归时，问题规模相比上闪递归都就有所减少
##递归效率不高，过多容易导致溢出
#
# def calc(n):
#     print(n)
#     return calc(n+1)
# calc(0)

def ccna(bn):
    print(bn)
    if int(bn/2) >0:
        return ccna(int(bn/2))
ccna(10)
