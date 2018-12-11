#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/11 10:26
# @Author: KeyJia
# @File: string.py

name = "my name is key"
print(name.count("a"))
print(name.capitalize())
print(name.center(20,"-"))
print(name.endswith("key"))
print(name.expandtabs(tabsize=30))
print(name.format(name))
# print(name.format_map({'name':'key':12}))
print(name.isalnum())

print('1A'.isdecimal())
print('1A'.isdigit())
print('a 1A'.isidentifier()) #判断是否是一个合法的标识符号
print('A'.islower())

print('331A'.isnumeric())
print('My Name Is Key'.istitle())
print('My Name Is Key'.isprintable()) #tty file ,drive file
print('+'.join(['1','2','3','4']))
print(name.ljust(50,'*'))

print("ABC".lower())
print("abc".upper())
print('  \n'.strip())

p = str.maketrans("abcd",'1234')
print("key abc".translate((p)))

print('key'.replace('e','c'))
print('1+2+3+4'.split('+'))
print('1+2+3+4'.swapcase())

print('key abc'.title())

print('key abc'.zfill(30))