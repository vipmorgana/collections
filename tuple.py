# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/29 17:51'

# 这说明python的名称只是一个指向 并不会占用内存
name_tuple = ('apple1', 'apple2')
name_tuple = ('apple2', 'apple3')

# 元祖拆包
user_tuple = ('apple', 29, 175)
name, age, height = user_tuple

user_tuple = ('apple', 29, 175, 'beijing')
name, *other = user_tuple

print(name, other)       # apple [29, 175, 'beijing']




