"""
8.14_实现自定义容器

你想实现一个自定义的类来模拟内置的容器类功能，比如列表和字典。但是你不确定到底要实现哪些方法

collections 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。
比如你想让你的类支持迭代，那就让你的类继承 collections.Iterable 即可
"""
import bisect
import collections


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        # 这里面使用到了 bisect 模块，它是一个在排序列表中插入元素的高效方式。可以保证元素插入后还保持顺序。
        bisect.insort(self._items, item)
