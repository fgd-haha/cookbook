"""
7.5_定义有默认参数的函数
"""


# 定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后
def spam1(a, b=42):
    print(a, b)


# 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None作为默认值
def spam2(a, b=None):
    if b is None:
        b = []


# 如果你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来，可以像下面这样写
# 这里对 object() 的使用看上去有点不太常见。object 是 python 中所有类的基类。
# 你可以创建 object 类的实例，但是这些实例没什么实际用处，因为它并没有任何有用
# 的方法，也没有任何实例数据 (因为它没有任何的实例字典，你甚至都不能设置任何属
# 性值)。你唯一能做的就是测试同一性。
_no_value = object()


def spam3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')



# 默认参数的值仅仅在函数定义的时候赋值一次。
x = 42
def spam4(b=x):
    print(b)

spam4()
x = 2
spam4()


# 默认参数的值应该是不可变的对象，比如 None、True、False、数字或字符串。特别的，千万不要像下面这样写代码
def spam5(b=[]):
    print(b)
    return b

x = spam5()
x.append(8)
spam5()
