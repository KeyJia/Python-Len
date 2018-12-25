#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/21 14:37
# @Author: KeyJia
# @File: json反序列化.py

import json

f = open("test.text","r")


for line in f:
    print(json.loads(line))


# data =json.load(f)
# print(data["func"]("keyJia"))
