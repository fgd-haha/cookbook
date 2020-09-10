"""
8.11_简化数据结构的初始化

你写了很多仅仅用作数据结构的类，不想写太多烦人的 init () 函数
"""


# 可以在一个基类中写一个公用的 init () 函数


class Structure1:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(self._fields) != len(args):
            raise TypeError('Expected: {} args'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


s = Stock(3, 4, 5)
print(s.__dict__)


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock2(Structure2):
    _fields = ['name', 'shares', 'price']


s1 = Stock2(3, 4, 5)
s2 = Stock2(3, 4, price=5)
s3 = Stock2(3, price=5, shares=4)

print(s1.__dict__, s2.__dict__, s3.__dict__)

