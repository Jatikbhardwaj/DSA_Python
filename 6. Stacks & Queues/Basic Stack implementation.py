class Stack:
    def __init__(self, capacity):
        """
        This Python function initializes a stack with a specified capacity.
        
        :param capacity: The `capacity` parameter in the `__init__` method is used to specify the maximum
        number of elements that the stack can hold. It is used to initialize the stack with a specific
        capacity and set the top index to -1 indicating an empty stack
        """
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def isEmpty(self):
        """
        The `isEmpty` function in Python checks if the top element of a stack is -1 to determine if the
        stack is empty.
        :return: The `isEmpty` method is returning a boolean value indicating whether the `top` attribute of
        the object is equal to -1.
        """
        return self.top == -1

    def isFull(self):
        """
        The function `isFull` checks if the stack is full by comparing the top index with the capacity minus
        one.
        :return: The `isFull` method is returning a boolean value indicating whether the stack is full or
        not. It checks if the `top` index of the stack is equal to `capacity - 1` and returns `True` if it
        is full, otherwise it returns `False`.
        """
        return self.top == self.capacity - 1

    def push(self, item):
        """
        The `push` function adds an item to the stack if it is not full, otherwise it raises an
        OverflowError.
        
        :param item: The `item` parameter in the `push` method represents the element that you want to add
        to the stack. When the `push` method is called, the `item` will be pushed onto the top of the stack
        if the stack is not full. If the stack is already full, an
        """
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = item
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        """
        The `pop` function removes and returns the top element of a stack if it is not empty, otherwise it
        raises an IndexError.
        :return: The `pop` method in the code snippet is returning the item that is being removed from the
        top of the stack.
        """
        if not self.isEmpty():
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            return None

    def size(self):
        return self.top + 1


stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.stack[:stack.size()])  # Output: [1, 2, 3]
print("Size:", stack.size())  # Output: 3
print("Peek:", stack.peek())  # Output: 3

popped_item = stack.pop()
print("Popped item:", popped_item)  # Output: 3
print("Stack after pop:", stack.stack[:stack.size()])  # Output: [1, 2]
