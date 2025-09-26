class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None 

    def is_empty(self):
        """Check if the queue is empty or not."""
        if self.head is None:
            return True
        return False

    def enqueue(self, data):
        """To add element at the end of the queue."""

        if self.head is None:
            node = Node(data)
            self.head = node
            return
        else:
            itr = self.head

            while (
                itr.next
            ):  # Here we have to be one step behind. Before going to the next address, first check whether there is a valid address or not.
                itr = itr.next
            node = Node(data)
            itr.next = node
            return

    def dequeue(self):
        """To remove the first element from the queue."""
        if self.head is None:
            return "Queue is empty, cannot dequeue."
        else:
            print(f"Dequeued element: {self.head.data}")
            self.head = self.head.next
            return

    def size(self):
        """Return the size of the queue."""
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        return length

    def display(self):
        """Displays the elements in queue."""
        if self.head == None:
            return "Queue is empty, add elements to display"
        itr = self.head
        index = 0
        while itr:
            print(f"{index}: {itr.data}")
            index += 1
            itr = itr.next


if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(f"Size of Queue: {q.size()}")

    print(f"Elements in queue: {q.display()}")

    q.dequeue()

    print(f"Elements in queue: {q.display()}")
