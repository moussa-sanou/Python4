class Node:
    # Define a function to initialize the attribute  and the pointer
    def __init__(self, data):
        self.data = data    # Data parameter
        self.next = None    # Next Pointer
        self.previous = None # Previous Pointer

    # Define a function for object representation
    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

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

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous =  new_previous


class DoublyLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head=>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
            size = 0
            # First check if the ll is empty is yes return 0 if no move to the next node
            if self.head is None:
                return 0
            # Create a variable representing the head of the ll
            current = self.head
            while current is not None:  # if current is not none there are some node left to count
                size += 1
                current = current.get_next()
            return size

    def search(self, data):
        if self.head is None:
            return "Linked list is empty. No Nodes to search."

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False

    def add_front(self, new_data):
        temp = Node(new_data)
        temp.set_next(self.head)

        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    def remove(self, data):
        if self.head is None:
            return "Linked List is empty. No nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()
        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())

dll = DoublyLL()
dll.size()
print(dll.size())
dll.add_front(1)
dll.head
print(dll.head)
dll.size()
print(dll.size())
dll.add_front(2)
dll.head
print(dll.head)
dll.size()
print(dll.size())