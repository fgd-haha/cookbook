"""在两个字典中寻找相同点"""
from pprint import pprint

a = {
    'foo': 1,
    'bar': 1,
    'car': 1,
}
b = {
    'foo': 2,
    'x': 1,
    'car': 1,
}
# 共同元素
print(a.keys() & b.keys())

# 属于a不属于b
print(a.keys() - b.keys())

# 使用字典推导式过滤元素
pprint({key: a[key] for key in a.keys() - {'a', 'bar'} if b[key] == 1})
