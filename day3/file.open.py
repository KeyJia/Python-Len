#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/12 11:20
# @Author: KeyJia
# @File: file.open.py

import os
import sys
f = open("yesterday",'r',encoding="utf-8")
for i in range(5):
    print(f.readline())


for line in f.readline():
    print(line.strip())

for index,line in enumerate(f.readline()):
    print(line.strip())
    if index == 9:
        print('-----------**-----------')
        continue
    print(line.strip)
