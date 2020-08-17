"""
列表推导式
filter
compress
"""
from itertools import compress

l1 = [2, 5, 67, -8, 8, -82, 2, 4, 5]
l2 = [2, 5, 67, 8, 'c', 'dk', 8, 82, 2, 4, 5, '_', '', ]

# 简单筛选
print([n for n in l1 if n > 0])

# 将筛选条件移到列表推导式中，替换不符合元素
print([n if n > 0 else 0 for n in l1])

# 列表数据大时，使用迭代器
l3 = (n for n in l1 if n > 0)
print(l3)
for i in l3:
    print(i)


# 复杂筛选使用filter
def is_int(item):
    try:
        int(item)
        return True
    except Exception:
        return False


l4 = filter(is_int, l2)
print(l4)
for i in l4:
    print(i)

# compress 接受一个可迭代对象，一个布尔选择器
address = [
    '中国，北京，大兴',
    '中国，北京，海淀',
    '中国，北京，朝阳',
    '中国，北京，丰台',
    '中国，北京，通州',
]

counts = [3, 2, 5, 7, 1]
more3 = [n > 3 for n in counts]
print(more3)
print(list(compress(address, more3)))
