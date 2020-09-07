"""
7.9_将单方法的类转换为函数

你有一个除 init () 方法外只定义了一个方法的类。为了简化代码，你想将它转换成一个函数。
"""

# 大多数情况下，可以使用闭包来将单个方法的类转换成函数。举个例子，下面示例中的类允许使用者根据某个模板方案来获取到 URL 链接地址
from urllib.request import urlopen


class UrlTemplate:

    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Example use. Download stock data from yahoo
yahoo = UrlTemplate(
    'https://search.jd.com/Search?keyword={keyword}&enc=utf-8&wq={keyword}&pvid=f210e43ce6d94ae8af0bd85cd5e0130b')
for line in yahoo.open(keyword='a'):
    print(line.decode('utf-8'))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


# Example use
yahoo = urltemplate('https://search.jd.com/Search?keyword={keyword}&enc=utf-8&wq={keyword}&pvid=f210e43ce6d94ae8af0bd85cd5e0130b')
for line in yahoo(keyword='a'):
    print(line.decode('utf-8'))
