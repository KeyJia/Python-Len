# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 10:44
# @Author  : KeyJia
# @File    : guess.py

age = 32
count = 0
while True:
    if count ==3:
        break
    guess_age = int(input("guess age:"))
    if guess_age == age:
        print("Yes you got it. ")
        break
    elif guess_age> age:
        print("think smaller...")
    else:
        print("think bigger!")

    count +=1








age = 32
count = 0
while count <3:
    guess_age = int(input("guess age:"))
    if guess_age == age:
        print("Yes you got it. ")
        break
    elif guess_age> age:
        print("think smaller...")
    else:
        print("think bigger!")
    count +=1






