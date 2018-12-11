#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/11 15:03
# @Author: KeyJia
# @File: dictionary.py

info = {
    'stu1101' : "key jia1",
    'stu1102' : "key jia2",
    'stu1103' : "key jia3",
}

# print(info) #字典是无序的
# #print(info["stu1101"])
#
# info ["stu1101"] = "武术"
# print(info)
#
# del info["stu1101"]
# print(info)
#
# info.pop("stu1102")
# print(info)
#
# info.popitem()
# print(info)

# b = {
#     'stu1101' : 'abc',
#     1:3,
#     2:5,
# }
# info.update(b)
# print(info.items())

for i in info:
    print(i,info[i])

c =  dict.fromkeys([6,7,8])#初始化值
print(c)


for k,v in info.items():
    print(k,v)

