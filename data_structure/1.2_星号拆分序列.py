""" 拆分可迭代对象使用*表示为一个列表 """
records = [
    ('foo', 1, 2),
    ('bar', 's'),
    ('foo', 5, 6),
]


def print_bar(s):
    print('bar:', s)


def print_foo(x, y):
    print('foo', x, y)


for tag, *args in records:
    print(*args)
    print(args)
    if tag == 'foo':
        print_foo(*args)
    elif tag == 'bar':
        print_bar(*args)
