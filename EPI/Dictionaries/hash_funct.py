
'''Implement a hash table from scratch using the ascii value to create a hash function'''

# hash fucntion
# ord() function will give us the ascii value of a character

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char) #sum of the ascii value of each character
    return h % 100 #divide the sum of the character ascii value by 100 which represent the size of the list we are using for this example

print(get_hash('march 22'))