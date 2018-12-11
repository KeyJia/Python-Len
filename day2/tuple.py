#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2018/12/10 16:26
# @Author: KeyJia
# @File: tuple.py

proudct_list = [
    ('iphone',5800),
    ('watch',9800),
    ('MAC pro',12000),
    ('Book',90),
]

shopping_list = []
salary = input("请输入你的工资:")
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in proudct_list:
        for index,item in enumerate(proudct_list):
            print(index,item)
        user_choice = input("请选择你的商品?")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(proudct_list) and user_choice >=0:
                p_item = proudct_list[user_choice]
                if p_item[1] <= salary: #买的起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" % (p_item, salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                print("product code [%s] is not exist!" % user_choice)
        elif user_choice == 'q':
            print('--------shopping  list -------')
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print("Invalid option")

