#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/7 12:27
# @Author: KeyJia
# @File: for.py


# for i in range(100):
#     print("loop",i)
#
#
# for k in range(0,10,3):
#     print("loop",k)


# for i in range(0,10):
#     if i <3:
#         print("loop",i)
#     else:
#         continue
#     print("hehe...")


for i in range(10):
    print('----------',i)
    for j in range(10):
        print(j)
        if j >5:
            break

