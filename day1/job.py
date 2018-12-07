#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/7 13:28
# @Author: KeyJia
# @File: job.py


_username = 'key'
_password = '123'
count = 0

username = input("usename:")
password = input("password:")
while count < 1:
    if username == _username and password == _password:
        print("welcome {name} login...".format(name=_username))
        break
    else:
        print("Invalid username or password!")
    count += 1