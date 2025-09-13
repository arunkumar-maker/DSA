class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.DELETE = "<DELETE>"
        self.table = [None] * size

    # This is first hash function
    def h1(self, key):
        return key % self.size

    # This is second hash function which gives us the step size to probe
    def h2(self, key):
        return 1 + ((key) % self.size - 1)

    def insert(self, key, value):
        index = self.h1(key)
        step = self.h2(key)

        i = 0

        while (
            self.table[index] != self.DELETE
            and self.table[index] != None
            and self.table[index] != key
        ):
            i += 1
            index = (self.h1(key) + i * step) % self.size

            if i == self.size:  # Completed checking all the slots
                raise Exception("hash table is full")

        self.table[index] = (key, value)

    def search(self, key):
        index = self.h1(key)
        step = self.h2(key)

        i = 0

        while self.table[index] != None:
            if self.table[index] != self.DELETE and self.table[index][0] == key:
                return self.table[index][1]  # returning the value of the searched key

            # if we are not able to find the value of key in first attempt then we have to probe the table to find it
            i += 1
            index = (self.h1(key) + i * step) % self.size
            if i == self.size:
                break
        return None

    def delete(self, key):
        index = self.h1(key)
        step = self.h2(key)

        i = 0

        while self.table[index] != None:
            if self.table[index] != self.DELETE and self.table[index] == key:
                self.table[index] = self.DELETE
                return True
            i += 1
            index = (self.h1(key) + i * step) % self.size
            if i == self.size:
                break
        return False

    def display(self):
        for i, value in enumerate(self.table):
            print(f"Index {i}: {value}")


ht = DoubleHashingHashTable(7)

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
