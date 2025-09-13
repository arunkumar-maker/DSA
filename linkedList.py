class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if not self.head:
            print("Linked list is empty.")

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + ("-->" if itr.next else "")
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if not self.head:
            node = Node(data)
            self.head = node
            return

        if self.head:
            node = Node(data, self.head)
            self.head = node
            return

    def insert_at_ending(self, data):
        itr = self.head

        if not self.head:
            node = Node(data)
            self.head = node
            return

        while (
            itr.next
        ):  # Here we have to be one step behind. Before going to the next address, first check whether there is a valid address or not.
            itr = itr.next
        node = Node(data)
        itr.next = node

    def delete_at_beginning(self):
        itr = self.head

        if not itr:
            print("Linked list is already empty.")
            return

        self.head = self.head.next

    def delete_at_ending(self):
        itr = self.head

        if not itr:  # If the list is already empty
            print("Linked list is already empty.")
            return

        while itr.next.next:  # always be one step behind
            itr = itr.next
        itr.next = None

    def remove_through_index(self, index):  # index will start from 0
        if index < 0 or index >= self.get_length():
            print("Invalid index")
            return

        if index == 0:
            self.delete_at_beginning()
            return

        if index == self.get_length() - 1:
            self.delete_at_ending()
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def remove_through_data(self, data):
        itr = self.head
        if self.head.data == data:
            self.head = self.head.next
            return

        while itr and itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        
        print("Given data is not present")

    def insert_at(self, index, data):  # index starts from zero (0)
        itr = self.head
        count = 0
        if index < 0 or index >= self.get_length():
            print("Invalid index")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, insert_after, data_to_insert):
        itr = self.head
        count = 0

        while itr:
            if itr.data == insert_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

        if count == self.get_length():
            print("Reached end of list. Inserting the data at the end.")
            self.insert_at_ending(data_to_insert)
            return


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(5)
    ll.insert_at_ending(10)
    ll.insert_at_beginning(12)
    ll.insert_at(1, 99)  # insert 99 at index 1
    ll.remove_through_index(2)  # remove element at index 2
    ll.delete_at_ending()  # delete last element
    ll.delete_at_beginning()  # delete first element
    ll.insert_at_beginning(22)
    ll.insert_at_beginning(33)
    ll.insert_at_beginning(44)

    ll.insert_after_value(444, 55)

    ll.remove_through_data(77)

    print("Length:", ll.get_length())
    ll.print()
