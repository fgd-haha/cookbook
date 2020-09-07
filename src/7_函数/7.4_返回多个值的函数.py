"""
7.4_返回多个值的函数

为了能返回多个值，函数直接 return 一个元组
"""


def myfun():
    return 1, 2, 3


a, b, c = myfun()
print(a)
print(b)
print(c)
