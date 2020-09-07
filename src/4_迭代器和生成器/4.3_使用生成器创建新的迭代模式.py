"""4.3_使用生成器创建新的迭代模式"""


def frange(start, stop, increment):
    """要有一个 yield 语句即可将其转换为一个生成器"""
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))
