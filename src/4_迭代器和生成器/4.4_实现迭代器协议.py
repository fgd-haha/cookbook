"""
4.4_实现迭代器协议
你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        """
        深度优先遍历
        它首先返回自己本身并迭代每一个子节点并通过调用子节点的 depth first() 方法 (使用 yield from 语句) 返回对应元素
        """
        yield self
        for c in self:
            yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)  # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
