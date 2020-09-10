"""
8.10_使用延迟计算属性

你想将一个只读属性定义成一个 property，并且只在访问的时候才会计算结果。但是一旦被访问后，你希望结果值被缓存起来，不用每次都去计算
"""
import math


class lazyproperty:
    """
    定义一个延迟属性的一种高效方法是通过使用一个描述器类
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, r):
        self.r = r

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.r ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.r


c = Circle(2)
print(vars(c), end='\n\n')

print(c.r, c.area, c.perimeter)
print(vars(c), end='\n\n')

print(c.r, c.area, c.perimeter)
