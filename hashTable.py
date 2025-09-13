class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        h = h % self.MAX
        return h

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (
                    key,
                    value,
                )  # here we are replacing the old tuple with the new tuple.
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == "__main__":
    ht = HashTable()
    ht["march 6"] = 243
    ht["march 7"] = 435
    ht["march 6"] = 123
    ht["march 17"] = 459
    ht["march 8"] = 773
    ht["march 9"] = 847

    del ht["march 17"]
    print(ht.arr)
