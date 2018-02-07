# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/2/7 14:29'

from collections import deque

# 1-1
# 原生的我们只能在尾部操作

user_list = ["apple1","apple2"]
user_name = user_list.pop()
print(user_name) # bobby2

# 1-2
# 用deque

user_deque = deque(("apple1","apple2"))
print(user_deque) # deque(['apple1', 'apple2'])

#1-3
user_deque = deque(("apple1","apple2"))
user_deque.appendleft("apple3")
print(user_deque) # deque(['apple3', 'apple1', 'apple2'])

# 1-4
user_deque2 = user_deque.copy()
user_deque2[1] = 'apple3'
print(user_deque,user_deque2) # deque(['apple3', 'apple1', 'apple2']) deque(['apple3', 'apple3', 'apple2'])
print(id(user_deque),id(user_deque2)) #35313120 35215320

# 1-5
user_deque = deque(["apple1",['apple1,apple2'],"apple2"])
user_deque2 = user_deque.copy()
user_deque2[1].append('apple1')
print(user_deque,user_deque2) # deque(['apple1', ['apple1,apple2', 'apple1'], 'apple2']) deque(['apple1', ['apple1,apple2', 'apple1'], 'apple2'])

# 1-6
# 深拷贝
import copy
user_deque2 = copy.deepcopy(user_deque)
user_deque2[1].append('apple1')
print(user_deque,user_deque2)  # deque(['apple1', ['apple1,apple2', 'apple1'], 'apple2']) deque(['apple1', ['apple1,apple2', 'apple1', 'apple1'], 'apple2'])

# 1-7
# 计算数量
user_deque = deque(["apple1",['apple1,apple2'],"apple2",'apple2'])
print(user_deque.count('apple2')) # 2

# 1-8
# 合并
user_deque = deque(["apple1",'apple3',"apple2"])
user_deque2 = deque(["apple1",'apple3',"apple2"])
user_deque.extend(user_deque2)
print(user_deque) # deque(['apple1', 'apple3', 'apple2', 'apple1', 'apple3', 'apple2'])

# 1-9
# 插入
user_deque = deque(["apple1",'apple3',"apple2"])
user_deque.insert(1, 'apple')
print(user_deque) # deque(['apple1', 'apple', 'apple3', 'apple2'])

# 1-10
# 剔除第一个元素
user_deque = deque(["apple1",'apple3',"apple2"])
user_deque.popleft()
print(user_deque) # deque(['apple3', 'apple2'])


'''
    import queue import Queue
    1，这个队列就是根据我们的deque来实现的
    2，deque是线程安全的，GIL的来保护的
    
'''