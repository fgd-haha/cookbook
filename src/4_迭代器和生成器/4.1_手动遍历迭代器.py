"""
4.1_手动遍历迭代器

"""


def manual_iter():
    """为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常"""
    with open('.\\temp.txt', mode='r', encoding='utf-8') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


manual_iter()


def manual_iter():
    """你还可以通过返回一个指定值来标记结尾，比如 None"""
    with open('.\\temp.txt', mode='r', encoding='utf-8') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')
