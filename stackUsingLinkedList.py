class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        """Push an item onto the stack which means adding the element into the beginning of the stack."""
        if self.head is None:
            self.head = Node(data, None)
            return
        node = Node(data, self.head)
        self.head = node

    def pop(self):
        """Pop an item from the beginning of the stack and returns the same."""
        if self.head is None:
            raise IndexError("pop from empty stack is not possible, stack underflow")
        print(f"Popped element: {self.head.data}")
        self.head = self.head.next
        return

    def is_empty(self):
        """check if the stack is empty or not"""
        if self.head is None:
            return True
        else:
            return False

    def peek(self):
        """returns the top most element of the stck without removing it."""
        if self.head is None:
            return "Stack is empty"
        else:
            return self.head.data

    def display(self):
        """Display the stack elements."""
        if self.head is None:
            return "Stack is empty"
        else:
            itr = self.head
            while itr:
                print(f"| {itr.data} |")
                itr = itr.next
            print("-----")


if __name__ == "__main__":
    s = stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.display()

    s.pop()
    s.pop()

    s.display()

    s.peek()
    print(f"Is stack empty? {s.is_empty()}")
    print(f"Top most element is: {s.peek()}")
