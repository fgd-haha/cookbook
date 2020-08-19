"""实现优先级队列"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)


q = PriorityQueue()
q.push('2343', 3)
q.push(('a', ), 3)
q.push('2343', 2)
q.push('1', 6)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
