import heapq

top_k = [3, 1, 5, 2, 4]

heapq.heapify(top_k)
print(heapq.heappop(top_k))
print(top_k)

"""
top K问题：
1. 插入排序
2. 使用堆排序
    2.1 建堆：填充完全二叉树，非叶节点，从下到上每一层与左右孩子节点比较，若孩子大，则交换。
    2.2 堆弹出，最后节点填充到顶，再下沉
    2.3 堆插入，添加到末尾，再上浮
3. 类似快排 复杂度O(n)
"""
