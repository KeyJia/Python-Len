#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/10 14:44
# @Author: KeyJia
# @File: name.py
import copy

names = ["abc","cde","def","pgf","kke"]

print(names[0:3]) #切片

#add
names.append("def")
names.insert(3,"abcde")

#remove
names.remove("abc")
print(names)

#pop
names.pop()
print(names)

#select
print(names[names.index("def")])

names.index("def")

#count
print(names.count("def"))

#sort
names.sort()
print(names)

#extend
names2 = [1,2,3,4,5]
names.extend(names2)
print(names)


name3 = ["abc","cde","ppod","ppoe"]
name4 = ["我是中国人"]
name5 = ["人民人民"]


for i in name5:
    print(i)

name7 = copy.deepcopy(name5)
print(name7)


print(name3[0:-1:2])
print(name3[::])