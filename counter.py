# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/7 14:59'

'''
    统计更屌
'''

from collections import Counter

users = ['apple1','apple2','apple1','apple3','apple2','apple2','apple4']

user_counter = Counter(users)
user_string = Counter('dasdasdfadfvsdfdasf')

print(user_string) # Counter({'d': 6, 'a': 4, 's': 4, 'f': 4, 'v': 1})
print(user_counter) # Counter({'apple2': 3, 'apple1': 2, 'apple3': 1, 'apple4': 1})

user_string.update('dadfadasda')

print(user_counter.most_common(2)) # [('apple2', 3), ('apple1', 2)]
print(user_string) # Counter({'d': 10, 'a': 8, 's': 5, 'f': 5, 'v': 1})