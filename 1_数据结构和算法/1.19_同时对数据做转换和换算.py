"""
使用迭代器时，可以省略一个（）
"""

nums = [1, 2, 3, 4, 5]

# 迭代器
print(i*i for i in nums)
# 列表
print([i*i for i in nums])
# 对迭代器进行运算，只需要一个（）
print(sum(i*i for i in nums))
print(min(i*i for i in nums))
# 对列表进行运算
print(sum([i*i for i in nums]))
print(min([i*i for i in nums]))
