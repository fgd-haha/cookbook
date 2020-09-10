"""
8.2_自定义字符串的格式化
"""

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        # format () 方法给 Python 的字符串格式化功能提供了一个钩子。这里需要着重强调的是格式化代码的解析工作完全由类自己决定。
        # 因此，格式化代码可以是任何值
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


date = Date(2020, 3, 3)
print(format(date))
print(format(date, 'mdy'))
