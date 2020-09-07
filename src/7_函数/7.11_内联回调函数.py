"""
7.11_内联回调函数

当你编写使用回调函数的代码的时候，担心很多小函数的扩张可能会弄乱程序控制流。你希望找到某个方法来让代码看上去更像是一个普通的执行序列
"""


# 通过使用生成器和协程可以使得回调函数内联在某个函数中。为了演示说明，假设你有如下所示的一个执行某种计算任务然后调用一个回调函数的函数
import sys
import time


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def add(x, y):
    return x + y


def print_result():
    sequence = 0

    def handle(result):
        nonlocal sequence
        sequence += 1
        print(sequence, result)

    return handle


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


@inlined_async
def test():
    # 内联回调函数
    handle = print_result()
    r = yield Async(add, (2, 3))
    handle(r)
    r = yield Async(add, ('hellow', 'world'))
    handle(r)
    for n in range(10):
        r = yield Async(add, (n, n + 1))
        handle(r)
    handle('end')


def test1():
    # 回调写法
    handle = print_result()
    apply_async(add, (2, 3), callback=handle)
    apply_async(add, ('hellow', 'world'), callback=handle)

    for n in range(10):
        apply_async(add, (n, n + 1), callback=handle)
    handle('end')


test()
test1()
