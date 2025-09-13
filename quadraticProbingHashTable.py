class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<DELETED>"

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        i = 1
        original_index = index

        while (
            self.table[index] is not None
            and self.table[index] != self.DELETED
            and self.table[index][0] != key
        ):

            index = (original_index + i * i) % self.size
            i += 1
            if i == self.size:  # tried all slots
                raise Exception("Hash Table is full!")

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        i = 1
        original_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            index = (original_index + i * i) % self.size
            i += 1
            if i == self.size:  # checked all slots
                break
        return None

    def delete(self, key):
        index = self.hash_function(key) 
        i = 1
        original_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            index = (original_index + i * i) % self.size
            i += 1
            if i == self.size:
                break
        return False

    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")


ht = QuadraticProbingHashTable(7)

ht.insert(10, "A")
ht.insert(20, "B")
ht.insert(30, "C")
ht.insert(17, "D")

print("Before deletion:")
ht.display()

print("\nSearch 17:", ht.search(17))
print("Search 99:", ht.search(99))

ht.delete(20)
print("\nAfter deleting 20:")
ht.display()
