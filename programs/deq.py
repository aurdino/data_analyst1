class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.items = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
