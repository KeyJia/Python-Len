#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/18 11:30
# @Author: KeyJia
# @File: decorator5.py

user ='keyjia'
passwd ='123'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("password:").strip()
        if user == username and passwd==password:
            print("username password authentication")
            func(*args,**kwargs)
        else:
            exit("user or password err")
        return wrapper

def index():
    print("welcome to index page")

def home():
    print("welcome to home page")
    return "from home"

def bbs():
    print("welcome to bbs page")

index()
print (home)
bbs()






