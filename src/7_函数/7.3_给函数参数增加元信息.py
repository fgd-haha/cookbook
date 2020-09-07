"""
7.3_给函数参数增加元信息

参数注解
"""

def add(x:int, y:int) -> int:
    return x + y

help(add)
print(add.__annotations__)
