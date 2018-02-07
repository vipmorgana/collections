# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/29 18:05'

from collections import namedtuple

'''
    namedtuple是tuple的一个子类，实际上2-1的这种方式创建的
    User对象是非常节省空间的，效率更高，Python解释器在解释
    class的时候会创建很多的变量的。
'''

'''
    我们在用mysqlclient，pymysql取数据的时候，实际上它就是
    一个tuple
'''
# 1-1
class User:
    def __init__(self, name, age, height):
        pass

# 2-1
User = namedtuple("User", ["name", "age", "height"])
user = User(name = 'apple', age=26, height=178)
print(user.age, user.name, user.height)    # 26 apple 178

# 3-1
User = namedtuple("User",["name", "age", "height"])
user_tuple = ("apple", 26,175)
user = User(*user_tuple)
print(user.age, user.name, user.height)    # 26 apple 175

# 函数参数
def ask(*args, **kwargs):
    pass

ask('apple', 26) # args = ('apple',26)

ask(name='apple',age=26) # kwargs = {'name':'apple','age':27}


# 4-1
User = namedtuple("User",["name", "age", "height"])
user_dict = {
    "name":'apple',
    'age' : 29,
    'height':175
}

user = User(**user_dict)

print(user.age, user.name, user.height) # 29 apple 175


# 5-1
'''
    这里面有个好处就是用_make就不需要使用*或者**了
'''
User = namedtuple("User",["name", "age", "height"])
user_tuple = ("apple", 26,179)
user = User._make(user_tuple)
print(user.age, user.name, user.height) # 26 apple 179

# 6-1
User = namedtuple("User",["name", "age", "height"])
user_tuple = ("apple", 26,175)
user = User(*user_tuple)
user_info_dict = user._asdict()  # OrderedDict([('name', 'apple'), ('age', 26), ('height', 175)])




