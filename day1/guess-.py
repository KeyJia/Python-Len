# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 10:44
# @Author  : KeyJia
# @File    : guess.py

boyage = 40
count = 0
while count <3:
    guess_age = int(input("guess_age:"))
    if guess_age == boyage:
        print("Yes,you got it .")
        break
    elif guess_age > boyage:
        print("think smaller...")
    else:
        print("think bigger!")
    count +=1
    if count == 3:
        countine_confirm = input("Do you wang to keep guessing...?")
        if countine_confirm !='n':
            count =0
else:
    print("you have tried too many times.. fuck off")







