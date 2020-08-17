"""从序列中移除重复项且保持元素间顺序不变"""

a = [1, 5, 2, 1, 8, 10]
b = [{'a': 2, 'b': 3}, {'a': 1, 'b': 3, 'c': 3}, {'a': 2, 'b': 3}]
# 去除重复，无序
print(list(set(a)))


def dedupe(items, key=None):
    """
    :param items: 要去重的对象
    :param key: 作用是指定一个函数将item变为可hash的对象
    :return:
    """
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            yield item
            s.add(val)


# item可hash，去除重复，有序
print(list(dedupe(a)))

# item不可hash，去除重复，有序
print(list(dedupe(b, lambda d: (d['a'], d['b']))))
