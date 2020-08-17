"""
namedtuple
命名元组：避免硬编码，与元素位置解耦，便于维护

注意：namedtuple不可变，若对数据有修改需求，使用字典
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['name', 'address'])
sub = Subscriber('hahaha', '北京大兴')
print(sub)
print(len(sub))
