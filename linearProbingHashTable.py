class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<DELETED>"

    def hash_function(self, key):
        h = key % (self.size)
        return h

    def insert(self, key, value):

        index = self.hash_function(key)
        original_index = index

        # here we have to check 2 conditions
        # 1. if the element is None then that means it is empty and we can insert the (key, value) tuple there.
        # 2. if the key which is already present in the element is matching (that means duplicate) then we have to update it.
        while (
            self.table[index] is not None
            and self.table[index] != self.DELETED
            and self.table[index][0] != key
        ):
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            index = (
                index + 1
            ) % self.size  # if we are not able to find then we have to do the incrementation linearly to the next cell.
            if (
                index == original_index
            ):  # after traversing the complete list and if we reach the starting point then we have to break and return None as we havent found anything.
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index] == key:
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")


lpht = LinearProbingHashTable(10)

lpht.insert(10, "A")
lpht.insert(20, "B")
lpht.insert(5, "C")
lpht.insert(15, "D")
lpht.insert(22, "E")

lpht.display()
