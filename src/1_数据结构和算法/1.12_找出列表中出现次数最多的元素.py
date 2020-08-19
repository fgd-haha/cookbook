"""
找出列表中出现次数最多的元素
Counter计数器使用
"""

from collections import Counter

words1 = ['sfk', 'sdlf', 'sdkf', 'sfk', 'sdlf', 'sfk', 'sdlf', 'sfk', 'sdlf', 'kd', 'csd', 'kd', 'kd', 'kd', 'kd',
          'book']
words2 = ['sdlf', 'kd', 'csd', 'kd', 'kd', 'kd', 'kd', 'book']
c1 = Counter(words1)
c2 = Counter(words2)

print(c1)  # Counter({'kd': 5, 'sfk': 4, 'sdlf': 4, 'sdkf': 1, 'csd': 1, 'book': 1})
# most_common 返回数量最多的前n个item
print(c1.most_common(1))  # [('kd', 5)]
print(c1.most_common(3))  # [('kd', 5), ('sfk', 4), ('sdlf', 4)]
# update可以增加计数
c1.update(['fl', 'kd'])
print(c1)

# Counter对象可以使用运算符 + -
c3 = c1 - c2
c4 = c1 + c2
print(c3)
print(c4)
