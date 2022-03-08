
# Let create a class representing all the node of our linked list

class node:
    # define the data variable and the pointer
    def __init__(self, data):
        self.data = data
        self.next = None

    # Add __rep__ for object representation
    def __repr__(self):
        return self.data

    # define a function capable of returning the data in the node
    def get_data(self):
        return self.data

    # Define a function that will set a new data in the node
    def set_data(self, new_data):
        # Replace the current value of the self.data with new_data
        self.data = new_data

    # Define the pointer of the node
    def get_next(self):
        return self.next

    # Define a function setting a new pointer which will replace the existing self.next value with a new one
    def set_next(self, new_next):
        self.next = new_next

# After creating a setting the parameters of the Node class we can start with our linked list class
class linkedList:
    # Define the init function
    def __init__(self):
        self.head = None

    # Define an object representation function
    def __repr__(self):
        return self.head

    # If we want to check if the linked list is empty
    def is_empty(self):
        return self.head is None

    # Define a function to add a new node to the front of the linkedlist
    def add_front(self, new_data):
        #declare the new data variable from the node class
        temp = node(new_data)
        #set the new variable as the head of the list
        temp.set_next(self.head)
        # Assigned the head of the node attribute to the new variable
        self.head = temp

    # To find the size of a linkedlist there a need to traverse LList and return an integer represent the number of nodes
    # The time complexity of finding the size of the llist is O(n) because every node must be visited in order to calculate the size of the llist
    def size(self):
        # if the llist is empty
        size = 0
        if self.head is None:
            return 0
        # Look if there are other nodes after the head node
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    # Search data in a linked list
    # The time complexity of searching a data in the llist is O(n) because every node must be visited in order to calculate the size of the llist
    def search(self, data):
        # for a search on an empty list
        if self.head is None:
            return "The Linked list is empty there is no node to search for"

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current.get_next()
        return False

    # Remove a node from a linked list
    def remove(self, data):
        # Empty llist
        if self.head is None:
            return "Empty llist no node to remove"

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with a data value is not present."
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def printNode(self):
        current = self.head
        while current:
            print(current.data)
            current = current.get_next()


N_node = node('apple')
print(N_node.get_data())