class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        else:
            itr = self.head
            dlstr = ""
            while itr:
                dlstr += str(itr.data) + ("-->" if itr.next else "")
                itr = itr.next
            print(dlstr)

    def get_length(self):
        itr = self.head
        if itr is None:
            print("Length of linked list id 0")
            return

        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data, next=self.head)
            self.head.prev = node
            self.head = node

    def insert_at_ending(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(data, prev=itr, next=None)
            itr.next = node

    def remove_at_beginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            self.head = self.head.next
            self.prev = None

    def remove_at_ending(self):
        if self.head is None:
            print("Linked list is empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.prev.next = None

    def insert_after_data(self, data_after, data_to_insert):
        if self.head is None:
            print("Linked list is empty so creating a node")
            node = Node(data_to_insert)
            self.head = node
        else:
            itr = self.head
            found = False
            while itr:
                if itr.data == data_after:
                    node = Node(data_to_insert, prev=itr, next=itr.next)
                    itr.next = node
                    found = True
                    break
                itr = itr.next

            if not found:
                print("Reached end of list, inserting at the end")
                self.insert_at_ending(data_to_insert)

    def remove_through_data(self, data):
        if self.head is None:
            print("Linked list is empty")
            return

        # Case 1: head is the node to delete
        if self.head.data == data:
            if self.head.next is None:  # only one node
                self.head = None
                return
            else:  # multiple nodes
                self.head = self.head.next
                self.head.prev = None
                return

        # Case 2: search in the rest of the list
        itr = self.head
        found = False

        while itr.next:
            if itr.next.data == data:
                to_delete = itr.next
                itr.next = to_delete.next
                if to_delete.next:  # not deleting the last node
                    to_delete.next.prev = itr
                found = True
                break
            itr = itr.next

        if not found:
            print("Link with the provided data is not available.")

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid index")
            return
        elif index == 0:
            self.remove_at_beginning()
            return
        elif index == self.get_length() - 1:
            self.remove_at_ending()
            return
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    if itr.next.next:
                        itr.next.next.prev = itr
                    break
                itr = itr.next
                count += 1


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.print()
    dll.insert_at_ending(20)
    dll.print()
    dll.insert_after_data(20, 30)
    dll.print()
    dll.insert_at_ending(40)
    dll.print()
    dll.insert_at_ending(50)
    dll.print()
    dll.remove_at_beginning()
    dll.print()
    dll.remove_at_ending()
    dll.print()
    dll.remove_at(2)
    dll.print()
    dll.remove_through_data(30)
    dll.print()
