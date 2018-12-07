#!/usr/bin/evn python
# -*-conding:utf-8 -*-

name = input("name:")
Age = input("Age:")
Job = input("Job:")
Salary = input("Salary:")


info ='''
--------- info  of %s-------
name:%s
Age:%s
Job:%s
Salary:%s
''' % (name,name,Age,Job,Salary)
print(info)



info2 = '''
------ info of {_name} ------
Name:{_name}
Age:{_Age}
Job:{_Job}
Salary:{_Salary}
'''.format(__name=name,
           __Age=Age,
           __Job=Job,
           __Salary=Salary)
print(info2)


