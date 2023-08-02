class node:
    data = None
    next = None
    prev=None

    def __init__(self, data):
        self.data = data

class circularLinklistFunction:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = node(data)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def display(self):
        if self.is_empty():
            print("Circular linked list is empty")
        else:
            current=self.head
            while True:
                print(current.data,end=" ")
                current=current.next
                if current == self.head:
                    break

cll=circularLinklistFunction()
cll.append(20)
cll.append(30)
cll.append(66)
cll.display()