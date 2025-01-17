class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        newNode = Node(data)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def isEmpty(self):
        return self.front is None
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        current = self.front
        while(current):
            print(current.data, end = "->")
            current = current.next
        print("None")

    def isEmpty(self):
        return self.front is None

    def deque(self):
        if self.isEmpty():
            print("Queue is Empty! nothiing to deque")
            return None
        else:
            remove = self.front.data
            self.front = self.front.next
        if self.front is None:
            self.rear = None
        return remove



if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.deque()
    q.display()
    