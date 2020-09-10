"""
8.9_创建新的类或实例属性

想创建一个全新的实例属性，可以通过一个描述器类的形式来定义它的功能。
"""


class Integer:
    """
    一个描述器就是一个实现了三个核心的属性访问操作 (get, set, delete) 的类，分别
为 get () 、 set () 和 delete () 这三个特殊的方法。这些方法接受一个实例
作为输入，之后相应的操作实例底层的字典。

    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        """
        get () 看上去有点复杂的原因归结于实例变量和类变量的不同。如果一个描述
器被当做一个类变量来访问，那么 instance 参数被设置成 None 。这种情况下，标准
做法就是简单的返回这个描述器本身即可 (尽管你还可以添加其他的自定义操作)
        :param instance:
        :param cls:
        :return:
        """
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    """
    为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中
    """
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.x, p.y)
p.x = 5
print(p.x, p.y)
print(Point.x)


# 下面是一些更高级的基于描述器的代码，并涉及到一个类装饰器
class Typed:
    def __init__(self, name, excepted_type):
        self.name = name
        self.excepted_type = excepted_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.excepted_type):
            raise TypeError('Excepted:', str(self.excepted_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, excepted_type in kwargs.items():
            setattr(cls, name, Typed(name, excepted_type))
        return cls

    return decorate


@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('apple', 23, 2.3)
print(s.__dict__)
del s.shares
print(s.__dict__)
