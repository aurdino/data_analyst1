class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def push(self, item):   
        # Push the item onto the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the item at the top of the stack
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        # Return the item at the top of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        ln = len(self.stack)
        return  True if  ln == 0 else False

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)
