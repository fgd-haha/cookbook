"""
ChainMap
可以将字典在逻辑上表现为一个单独的字典，实际上，ChainMap只是维护了一个记录底层映射关系的表
"""

from collections import ChainMap

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
c = ChainMap(a, b)

print(len(c))  # 3
print(c['x'])  # 1
# 两个字典中相同的元素，会使用第一个字典中的值
print(c['y'])  # 2
print(c['z'])  # 4

# 修改操作仅作用在第一个字典上
c['x'] = 5
print(c['x'], a['x'])  # 5 5
c['y'] = 5
print(c['y'], a['y'], b['y'])  # 5 5 3
c['z'] = 5  # a字典新加一个键值对，b字典不变
print(c['z'], a['z'], b['z'])  # 5 5 4
