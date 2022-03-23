
class Node:
    # Define constructor
    def __init__(self, data, next):
        self.data = data
        self.next =  next

# Creating the linked list class with a singly head node
class LinkedList:
    def __init__(self):
        self.head = None