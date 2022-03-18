class Node:
    # Define a function to initialize the attribute  and the pointer
    def __init__(self, data):
        self.data = data    # Data parameter
        self.next = None    # Next Pointer
        self.previous = None # Previous Pointer

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

    def get_previous(self):
        return self.previous

    def set_previous(self, new_previous):
        self.previous =  new_previous
