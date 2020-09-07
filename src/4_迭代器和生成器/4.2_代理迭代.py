"""
4.2_代理迭代
构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直
接在你的这个新容器对象上执行迭代操作
"""


class Node:
    """实际上你只需要定义一个 iter () 方法，将迭代操作代理到容器内部的对象上去"""

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        """ iter () 方法只是简单的将迭代请求传递给内部的 children属性"""
        # iter(s) 只 是 简 单 的 通 过 调 用s. iter () 方法来返回对应的迭代器对象，就跟 len(s) 会调用 s. len () 原理是一样的
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)
