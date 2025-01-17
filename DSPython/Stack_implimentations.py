#stack implimentation by list
stack = []
stack.append("1")
stack.append("A")
stack.append("2")

print("Initial stack",stack)
stack.pop()
print("After pop",stack)
stack.pop()
stack.pop()
print("After pop",stack)

#implimentation using collection.dequeue
from collections import deque

stack = deque()
stack.append("1")
stack.append("2")
stack.append("3")
print("Initial deque stack",stack)
stack.pop()
print("After deque pop",stack)

#implimentation using queue module
from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print(stack.qsize())

stack.put("a")
stack.put("b")
stack.put("c")

print(stack.qsize())

print("Full: ", stack.full())
print("Size: ", stack.qsize())

print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

#implimention using Linkedlist
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]


    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from the Empty stack!")

        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value

    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value
    
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for j in range(1, 6):
        top_value = stack.pop()
        print(f"Poped value: {top_value}")

    print(f"Stack: {stack}")
   











