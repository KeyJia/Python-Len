#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/13 14:52
# @Author: KeyJia
# @File: file_change.py

f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday3","w",encoding="utf-8")

for line in f:
    if "舌尖泪水的苦涩滋味" in line:
        line = line.replace("舌尖泪水的苦涩滋味","舌尖泪水的苦涩滋味==")
        f_new.write(line)
f.close()
f_new.close()


# with open("yesterday2","r",encoding="utf-8") as f:
#         for line in f:
#             print(line)
