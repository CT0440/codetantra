class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newnode = Node(data)
        if (self.head is None):
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def printList(self):
        if self.head is None:
            print("There are no nodes are present")
        else:
            cur = self.head
            while(cur):
                print(cur.data, end = "->")
                cur = cur.next
            print("None")

    def insertAtPosition(self, position, data):
        if position < 0:
            print("Position must be non-negative integer.")
            return
        newnode = Node(data)
        if position == 0:
            self.insertAtBeginning(data)
            return
        cur = self.head
        count = 0
        while cur and count < position - 1:
            cur = cur.next
            count += 1
        if cur is None:
            print(f"Position {position} out of bounds")
            return

        newnode.next = cur.next
        cur.next = newnode

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            newnode = self.head
            return
        cur = self.head
        while (cur.next):
            cur = cur.next
        cur.next = newnode 
    

if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.insertAtBeginning(1)
    sll.insertAtBeginning(2)
    sll.insertAtBeginning(3)
    sll.insertAtPosition(2, 7)
    sll.insertAtEnd(100)
    sll.printList()
    


