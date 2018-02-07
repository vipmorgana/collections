# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/7 15:06'

from collections import OrderedDict

user_dict = OrderedDict()
user_dict['b'] = 'apple1'
user_dict['a'] = 'apple2'
user_dict['c'] = 'apple3'
print(user_dict)  # OrderedDict([('b', 'apple1'), ('a', 'apple2'), ('c', 'apple3')])

'''
    Python3里面默认就是有序的，Python2不是有序的
'''

print(user_dict.popitem()) # ('c', 'apple3')
print(user_dict.pop('a')) # apple2

user_dict = OrderedDict()
user_dict['b'] = 'apple1'
user_dict['a'] = 'apple2'
user_dict['c'] = 'apple3'
print(user_dict)

print(user_dict.move_to_end("b"))
print(user_dict) # OrderedDict([('a', 'apple2'), ('c', 'apple3'), ('b', 'apple1')])