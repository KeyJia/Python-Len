#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/12 15:33
# @Author: KeyJia
# @File: 进度条

import sys,time
for i in range(99):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)
