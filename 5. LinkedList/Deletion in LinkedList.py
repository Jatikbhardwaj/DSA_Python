class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def deleteAtStart(self):
        if self.head is None:
            print("Empty List, nothing to delete")
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("Empty List, nothing to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.deleteAtStart()
            return
        current = self.head
        for _ in range(position - 1):
            if current is None or current.next is None:
                print("Invalid position")
                return
            current = current.next
            current.next = current.next.next

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)


llist = LinkedList()
llist.insertAtEnd(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtEnd(40)
llist.delete_at_position(2)
llist.printlinkedlist()
