"""
8.20_通过字符串调用对象方法

你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法

最简单的情况，可以使用 getattr()

另外一种方法是使用 operator.methodcaller()
"""

import math
from pprint import pprint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)

import operator

operator.methodcaller('distance', 0, 0)(p)

# 当你需要通过相同的参数多次调用某个方法时，使用 operator.methodcaller 就
# 很方便了。比如你需要排序一系列的点，就可以这样做：
points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]
# Sort by distance from origin (0, 0)
points.sort(key=operator.methodcaller('distance', 0, 0))
pprint(points)
