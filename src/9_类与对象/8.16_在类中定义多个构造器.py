"""
8.16_在类中定义多个构造器

你想实现一个类，除了使用 init () 方法外，还有其他方式可以初始化它。
为了实现多个构造器，你需要使用到类方法。
"""
import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)  # Primary
b = Date.today()  # Alternate
