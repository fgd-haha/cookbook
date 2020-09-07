"""
7.2_只接受关键字参数的函数

希望函数的某些参数强制使用关键字参数传递
"""


def recv(maxsize, *, block):
    'Receives a message'
    pass


# recv(1024, True)  # TypeError
recv(1024, block=True)  # Ok


def mininum(*values, clip=None):
    """
    利用这种技术，我们还能在接受任意多个位置参数的函数中指定关键字参数
    :param values:
    :param clip:
    :return:
    """
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(mininum(1, 5, 2, -5, 10))  # Returns -5
print(mininum(1, 5, 2, -5, 10, clip=0))  # Returns 0

# 使用强制关键字参数也会比使用 **kwargs 参数更好，因为在使用函数 help的时候输出也会更容易理解
help(recv)
