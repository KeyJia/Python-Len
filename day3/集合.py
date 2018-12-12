#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/12 10:36
# @Author: KeyJia
# @File: 集合.py
list_1 = set([1,0,20,60,90,21])
list_2 = set([2,0,60,40,80,24])
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))

#并集
print(list_1.union(list_2))

#差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))

#子集
print(list_2.issubset(list_1))

#
list_3 = set ([1,3,7])
print(list_3.issuperset(list_1))
print(list_3.issubset(list_1))

# 反向差集对称差集
print(list_1.symmetric_difference(list_2))

print("--------------")
list4 = set([32,55,22,])
print(list_3.isdisjoint(list4))

#交集
print(list_1&list_2)
#union
print(list_1 | list_2)

#对称差集
print(list_1 ^ list_2)

#add
list_1.add(90)


list_1.update([1,3,5,6,7,8])

print(list_1)


