# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/29 18:05'

from collections import namedtuple


class User:
    def __init__(self, name, age, height):
        pass

User = namedtuple("User", ["name", "age", "height"])
user = User(name = 'apple', age=26, height=178)

print(user.age, user.name, user.height)    # 26 apple 178

