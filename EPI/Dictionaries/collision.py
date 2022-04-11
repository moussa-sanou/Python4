
# Creating a hash table with collision handling

class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [ [] for i in range(self.Max)]

    #Hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    # Create a function to add key value pair in the hash table
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    # Create a function to get key value
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
