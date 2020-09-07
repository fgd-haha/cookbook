"""
7.12_访问闭包中定义的变量

通常来讲，闭包的内部变量对于外界来讲是完全隐藏的。但是，你可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现这个目的。
"""


def sample():
    n = 0

    # Closure function
    def func():
        nonlocal n
        n += 1
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n

    return func


s = sample()
s()
print(s.get_n())
s.set_n(8)
print(s.get_n())
