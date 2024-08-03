class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_loop(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        else:
            visited.add(current)
            current = current.next
    return False


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1

print(has_loop(node1))
