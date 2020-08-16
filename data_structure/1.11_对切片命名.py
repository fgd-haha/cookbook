"""对切片命名，slice，indices使用"""

records = '**********100**********23.32*****'

# 硬编码：
cost = int(records[10:13]) * float(records[23:28])
print(cost)

# 使用切片对象,避免硬编码索引
SHARES = slice(10, 13, 1)
PRICE = slice(23, 28)
cost = int(records[SHARES]) * float(records[PRICE])
print(SHARES.start, SHARES.stop, SHARES.step)
print(cost)


# indices 使用，对切片对象裁剪，防止越界
a = slice(2, 50, 2)
s = 'helloworld'
print(a.indices(len(s)))
print(*a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])

