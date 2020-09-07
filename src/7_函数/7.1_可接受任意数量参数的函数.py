"""
7.1_可接受任意数量参数的函数
"""

import html


def avg(first, *rest):
    """求平均数"""
    return (first + sum(rest)) / (1 + len(rest))


# Sample use
print(avg(1))  # 1.0
print(avg(1, 2))  # 1.5
print(avg(1, 2, 3, 4))  # 2.5


def make_element(name, value, **attrs):
    """生成html节点"""
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))
# Creates '<p>&lt;spam&gt;</p>'
print(make_element('p', '<spam>'))



