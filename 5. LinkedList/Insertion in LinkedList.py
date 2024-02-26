class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtPosition(self, data, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.insertAtStart(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Invalid Position")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.insertAtEnd(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtStart(100)
llist.insertAtStart(500)
llist.insertAtPosition(999, 2)
llist.printLinkedList()
