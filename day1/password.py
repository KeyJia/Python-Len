# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 10:30
# @Author  : KeyJia
# @File    : password.py.py

import os
_username = 'keyjia'
_password = '123'

username = input("usename:")
password = input("password:")

if _username == username and _password == password:
    print("welcome user{name} login...".format(name=_username))
else:
    print("Invalid username or password!")
