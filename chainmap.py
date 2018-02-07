# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/7 15:16'

from collections import ChainMap

user_dict1 = {"a":"apple1", "b":"apple2"}
user_dict2 = {"c":"apple2", "d":"apple3"}

# 1-1
for key, value in user_dict1.items():
    print(key,value)

for key, value in user_dict2.items():
    print(key,value)

#1-2
'''
    a apple1
    d apple3
    c apple2
    b apple2
'''
new_dict = ChainMap(user_dict1,user_dict2)
for key, value in new_dict.items():
    print(key,value)

#1-3

print(new_dict.maps) # [{'a': 'apple1', 'b': 'apple2'}, {'c': 'apple2', 'd': 'apple3'}]