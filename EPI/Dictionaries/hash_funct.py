
'''Implement a hash table from scratch using the ascii value to create a hash function'''

# hash fucntion
# ord() function will give us the ascii value of a character
#
# def get_hash(key):
#     h = 0
#     for char in key:
#         h += ord(char) #sum of the ascii value of each character
#     return h % 100 #divide the sum of the character ascii value by 100 which represent the size of the list we are using for this example
#
# print(get_hash('march 22'))

# Creating a hash table

class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    #Hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    # Create a function to add key value pair in the hash table
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

t = HashTable()
t['march 6'] = 130
print(t['march 6'])