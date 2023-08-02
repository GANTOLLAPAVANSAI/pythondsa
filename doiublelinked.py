class node:
    data = None
    next = None
    prev=None

    def __init__(self, data):
        self.data = data

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    
    def createdbll(self, data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next=self.head
            new_node.prev=self.head
        else:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next=self.head
            self.head.prev=new_node

    def display(self):
        if self.is_empty():
            print("The list is empty.")
        else:
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break
            print()
           # print(current.prev.data)

dll = DoublyLinkedList()
dll.createdbll(77)
dll.createdbll(99)
dll.createdbll(88)
dll.display() 
print()