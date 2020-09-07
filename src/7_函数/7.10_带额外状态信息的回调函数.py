"""
7.10_带额外状态信息的回调函数

（1）使用类存储额外状态信息
（2）使用闭包
（3）使用协程
"""


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)


def add(x, y):
    return x + y


def print_result(result):
    """
    不带状态的普通回调函数
    :param result:
    """
    print(result)


apply_async(add, (1, 2), callback=print_result)


class ResultHandler:
    """
    （1）使用类存储额外状态信息的回调函数
    """
    sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('{}: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, ('hello', 'world'), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)


def make_handler():
    """
    (2) 使用闭包
    :return:
    """
    sequence = 0

    def result_handler(result):
        nonlocal sequence  # 不声明nonlocal的话，内部函数只能访问不能修改
        sequence += 1
        print('{}: {}'.format(sequence, result))

    return result_handler


handler = make_handler()
apply_async(add, ('hello', ' hahaha'), callback=handler)
apply_async(add, ('hello', ' hehehe'), callback=handler)


def make_handler():
    """
    (3) 使用协程
    :return:
    """
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('{}: {}'.format(sequence, result))


handler = make_handler()
next(handler)
apply_async(add, ('hello', '  协程1'), callback=handler.send)
apply_async(add, ('hello', '  协程2'), callback=handler.send)
