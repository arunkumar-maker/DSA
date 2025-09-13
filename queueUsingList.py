class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the list is empty or not."""
        if len(self.items) == 0:
            return True
        return False

    def enqueue(self, item):
        """To add the element at the end of the list."""
        if item is None:
            raise ValueError("Cannot add invalid values to the queue")
        self.items.append(item)

    def dequeue(self):
        """To remove the element from the beginning of the List as this is a QUEUE."""
        if self.is_empty():
            return "Queue is empty, cannot dequeue"
        else:
            del self.items[0]
            return self.items

    def size(self):
        """Return the size of the queue."""
        return len(self.items)

    def display(self):
        """Displays the elements in queue."""
        if len(self.items) == 0:
            return "Queue is empty, add elements to display"
        for i, val in enumerate(self.items):
            print(f"{i}: {val}")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(f"Size of Queue: {q.size()}")
    print()
    print(f"Elements in queue: {q.display()}")

    q.dequeue()
    print(f"Elements in queue: {q.display()}")
