class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        cur = self.head
        while (cur):
            print(cur.data)
            cur = cur.next

if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.head= Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.printList()