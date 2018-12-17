#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/17 11:31
# @Author: KeyJia
# @File: 局部变量.py

# school = 'Tj edu.'
#
#
#
# def change_name(name):
#     print("before change",name,school)
#     name ="KEY JIA"
#     age = 21
#     print("after change",name)
#
# name = "keyjia"
# change_name(name)
# print(name)
#
# names = ["keyjia","jia1","Rain"]
# names_tuple = (1,2,3,4)
# def chage_name():
#     names[0] = "网络人"
#     print("aaa",names)

##递归

def calc(n):
    print(n)
    if int(n/2) == 0:
        return 0
    return calc(int(n/2))
calc(10)