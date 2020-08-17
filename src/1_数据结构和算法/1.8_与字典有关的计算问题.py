"""与字典有关的计算问题： 最小值，最大值，排序等
    使用zip将键值对反置，进行比较
"""

prices = {
    'a': 1,
    'b': 2,
    'c': 1.1,
    'd': 0.1,
    'e': 3,
    'f': 1,
}

# 计算价格最低的股票：
print(min(prices, key=lambda k: prices[k]))  # 获取键
print(prices[min(prices, key=lambda k: prices[k])])  # 获取值
print(min(zip(prices.values(), prices.keys())))  # 获取键值

# 按价格排序
print(sorted(zip(prices.values(), prices.keys())))

# 需要注意zip是迭代器，只能使用一次
prices_zip = zip(prices.values(), prices.keys())
print(min(prices_zip))
print(max(prices_zip))  # 这里将抛出异常
