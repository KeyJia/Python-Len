#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/10 16:14
# @Author: KeyJia
# @File: test.py

import copy

person =['name',['saving',100]]

# p1=copy.copy(person)
#
# p2=person[:]
#
# p3=list(person)

p1 = person[:]
p2 = person[:]


p1[0]='key'
p2[0]='feng'


p1[1][1]=50

print(p1)
print(p2)

