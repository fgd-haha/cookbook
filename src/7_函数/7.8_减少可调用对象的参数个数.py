"""
7.8_减少可调用对象的参数个数
（1）使用functools.partial()
（2）使用lamda表达式
"""
from functools import partial
from pprint import pprint

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
import math


def distance(p1, p2):
    """计算两点间距离"""
    x1, y1 = p1
    x2, y2 = p2

    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)


# 根据到pt点的距离排序,sort只能接受只有一个入参的函数
def a(x):
    return x[1]


points.sort(key=a, reverse=True)
print(points)

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
points.sort(key=partial(distance, pt))
print(points)

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
points.sort(key=lambda x: distance(pt, x))
print(points)
