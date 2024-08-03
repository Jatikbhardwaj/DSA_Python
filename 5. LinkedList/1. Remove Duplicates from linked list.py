class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = LinkedListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


def removeDuplicatesFromLinkedList(linkedlist):
    currentNode = linkedlist.head
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while (
                nextDistinctNode is not None and nextDistinctNode.value == currentNode.value
        ):
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedlist


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(4)

# Print the original linked list for debugging
print("Original Linked List:")
my_linked_list.print_list()

# Remove duplicates
removeDuplicatesFromLinkedList(my_linked_list)

# Print the modified linked list for debugging
print("Linked List after Removing Duplicates:")
my_linked_list.print_list()
