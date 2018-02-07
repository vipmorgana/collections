# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/7 14:11'

'''
    defaultdict是用C语言完成的
'''

from collections import defaultdict

# 我们先用dict完成一个list元素出现个数的统计功能
# 1-1
users = ['apple1','apple2','apple1','apple3','apple2','apple2','apple4']

user_dict = {}
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1

print(user_dict)  # {'apple1': 2, 'apple2': 3, 'apple3': 1, 'apple4': 1}

# 1-2
# setdefault可以让我们的代码变的更少，不需要做if判断，
# 性能也更高
users = ['apple1','apple2','apple1','apple3','apple2','apple2','apple4']
user_dict = {}
for user in users:
    user_dict.setdefault(user, 0)
    user_dict[user] += 1
print(user_dict)  # {'apple1': 2, 'apple2': 3, 'apple3': 1, 'apple4': 1}


# 1-3
# 实际上下面这种写法的严谨性更高了
default_dict = defaultdict(int)
users = ['apple1','apple2','apple1','apple3','apple2','apple2','apple4']
for user in users:
    default_dict[user] += 1
print(default_dict) # {'apple1': 2, 'apple2': 3, 'apple3': 1, 'apple4': 1}

#1-4
'''
    defaultdict(<function gen_default at 0x03E7C348>, {'group1': {'name': '', 'nums': 0}})
'''
def gen_default():
    return {
        "name": "",
        "nums": 0
    }

default_dict = defaultdict(gen_default)
default_dict["group1"]
pass

