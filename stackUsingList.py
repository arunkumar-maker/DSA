class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack which means adding the element into the beginning of the list."""
        self.stack.insert(0, item)

    def pop(self):
        """Pop an item off the stack which means removing the first element of the list."""
        if not self.is_empty():
            return self.stack.pop(0)
        raise IndexError("pop from empty stack, stack underflow")

    def peek(self):
        """return the element from the top but not remove it"""
        if len(self.stack) == 0:
            return "Empty stack"
        else:
            return self.stack[0]

    def is_empty(self):
        """Check if the stack is empty."""
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        """return the size of the stack"""
        return len(self.stack)

    def display(self):
        """Display the stack."""
        if self.size() == 0:
            return "Empty stack"
        if self.size() == 1:
            return f"Top -> {self.stack[0]}"
        else:
            for val in self.stack:
                print(f"| {val} |")

            print("-----")

if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()
    s.pop()
    s.display()
    print(s.peek())
    print(f"Status of stack: {s.is_empty()}")
