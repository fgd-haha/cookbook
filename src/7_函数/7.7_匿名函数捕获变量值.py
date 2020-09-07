"""
7.7_匿名函数捕获变量值
"""

# lambda表达式运行时绑定x值，所以a，b函数的x都是20
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))  # 30
print(b(10))  # 30

x = 30
print(a(10))  # 40

# 定义默认参数，则在定义时绑定值
x = 10
a1 = lambda y, x=x: x + y
x = 20
b1 = lambda y, x=x: x + y
print(a1(10))  # 20
print(b1(10))  # 30

funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))  # 打印5个4

funcs2 = [lambda x, n=n: x + n for n in range(5)]
for f in funcs2:
    print(f(0))  # 打印0 1 2 3 4 5
