"""
8.1_改变对象的字符串显示

要改变一个实例的字符串表示，可重新定义它的 str () 和 repr () 方法。
"""


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # format() 方法的使用看上去很有趣，格式化代码 {0.x} 对应的是第 1 个参数的 x 属性。因此，0 实际上指的就是 self 本身
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


# __repr__ () 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。内置的 repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。
# __str__()方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串。
# 特别来讲，!r 格式化代码指明输出使用 repr () 来代替默认的 str ()
p = Pair(3, 4)
print('{}'.format(p))
print('{!r}'.format(p))
