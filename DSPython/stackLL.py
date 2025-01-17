class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while (cur):
            out += str(cur.value + "->")
            cur = cur.next

    

def push(self, value):
    node = Node(value)
    node.next = self.head.next
    self.head.next = node
    self.size += 1

def pop(self):
    if self.isEmpty(self):
        raise Exception("Popping from the Empty Stack!")
    remove = self.head.next
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
    print("Stack elements: {stack}")

    for j in range (1, 6):
        poppedItem = stack.pop()
    print("popped Elements : {pop}")
