#queue implimentation using list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print('Initial queue')
print(queue)
print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("After removing Elements:")
print(queue)

#queue implimentation using Collections dequeue
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('susruthi')
print("displaying the queue elements:")
print(q)
print("removing the elements")
print(q.popleft())

#implimentation using Queue


