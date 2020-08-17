from collections import deque
# 双向链表

# 不设maxlen则无限大
q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)

# 先进先出
q.append(4)
print(q)
