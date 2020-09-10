"""
8.7_调用父类方法

调用父类 (超类) 的一个方法，可以使用 super() 函数
"""


# super() 函数的一个常见用法是在 init () 方法中确保父类被正确的初始化了
class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


# super() 的另外一个常见用法出现在覆盖 Python 特殊方法的代码中
class Proxy:
    """
     setattr () 的实现包含一个名字检查。如果某个属性名以下划
线 ( ) 开头，就通过 super() 调用原始的 setattr () ，否则的话就委派给内部的代
理对象 self. obj 去处理。这看上去有点意思，因为就算没有显式的指明某个类的父
类， super() 仍然可以有效的工作。
    """

    def __init__(self, obj):
        self._obj = obj
        # Delegate attribute lookup to internal obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # Call original __setattr__
        else:
            setattr(self._obj, name, value)


# 不推荐写法，可能多次调用基类初始化
class Base:
    def __init__(self):
        print('Base.__init__')


class A1(Base):
    def __init__(self):
        Base.__init__(self)
        print('A1.__init__')


class B1(Base):
    def __init__(self):
        Base.__init__(self)
        print('B1.__init__')


class C1(A1, B1):
    def __init__(self):
        A1.__init__(self)
        B1.__init__(self)
        print('C1.__init__')


c = C1()  # Base A1 Base B1 C1


class Base:
    def __init__(self):
        print('Base.__init__')


class A2(Base):
    def __init__(self):
        super().__init__()
        print('A2.__init__')


class B2(Base):
    def __init__(self):
        super().__init__()
        print('B2.__init__')


class C2(A2, B2):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C2.__init__')


print('\n')
c = C2()  # Base B2 A2 C2

"""
我们需要花点时间解释下 Python 是如何实现继承的。对于你
定义的每一个类，Python 会计算出一个所谓的方法解析顺序 (MRO) 列表。这个 MRO
列表就是一个简单的所有基类的线性顺序表。
C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
<class '__main__.Base'>, <class 'object'>)
为了实现继承，Python 会在 MRO 列表上从左到右开始查找基类，直到找到第一
个匹配这个属性的类为止。
"""
