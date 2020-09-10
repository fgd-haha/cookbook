"""
8.12_定义接口或者抽象基类

你想定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法
"""
import io
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    """
    使用 abc 模块可以很轻松的定义抽象基类
    """

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 抽象类的一个特点是它不能直接被实例化
# a = IStream()  # TypeError: Can't instantiate abstract class IStream with abstract methods read, write


def serialize(obj, stream):
    """
    抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口
    :param obj:
    :param stream:
    :return:
    """
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


IStream.register(io.IOBase)
