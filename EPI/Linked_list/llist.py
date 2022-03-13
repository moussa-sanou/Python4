
'''Create a Node Class'''

class Node:
    # Define a function to initialize the attribute  and the pointer
    def __init__(self, data):
        self.data = data    # Data parameter
        self.next = None    # Pointer

    # Define a function for object representation
    def __repr__(self):
        return self.data

    # Define a function to return the self.data attributes
    def get_data(self):
        return self.data

    # Define a function that can replace the existing value of self.data with a new_data parameter
    def set_data(self, new_data):
        self.data = new_data

    # Define function pointing to the next node which will returns the self.next attribute
    def get_next(self):
        return self.next

    # Define a function to change the existing value or direction of the pointer to a new pointer
    def set_next(self, new_next):
        self.next = new_next


''' Create a singly linkedlist'''
# LinkedList do not contain nodes instead they have a head attribute that point to the first node the linkedlist if one exist

class Singlyllist:

    # Define a function representing the first node of the linkedlist
    def __init__(self):
        self.head = None

    # Define a function for object representation
    def __repr__(self):
        return self.head

    # Define a function to check if the LL is empty it will return True or False if the ll is empty or not
    def is_empty(self):
        return self.head is None

    # Define a function to add a node at the front of the LL
    def add_front(self, new_data):
        # Create a new node
        temp = Node(new_data)
        # Change the pointer of the temp node to point to the self.head
        temp.set_next(self.head)
        # Now we need to assign the temp variable as the head of the ll
        self.head = temp

    # Check the size of a ll the function will traverse the ll and return an integer value representing the number of nodes in the ll
    def size(self):
        size = 0
        # First check if the ll is empty is yes return 0 if no move to the next node
        if self.head is None:
            return 0
        # Create a variable representing the head of the ll
        current = self.head
        while current is not None: # if current is not none there are some node left to count
            size += 1
            current = current.get_next()
        return  size

sll = Singlyllist()
sll.size()
print(sll.size())
sll.add_front(1)
sll.add_front(2)
sll.add_front(3)
sll.add_front(1)

print(sll.size())

