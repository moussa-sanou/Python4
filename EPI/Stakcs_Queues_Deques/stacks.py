class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        '''Accepts an item as a paramater and appends it to the end of the list. Returns nothing.
        The runtime for this method is o(1), or constant time, because appending to end of a list happens in constant time.'''

        self.items.append(item)

    def pop(self):
        '''Removes and return the last item for the list, which is also the top item of the stack.
         The runtime here is constant time, because all it does is index to the last item of the list.'''
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        '''This method returns the last item in the list, which is also the item at the top of the stack.
        This method runs in constant time because indexing into a list is done in constant time.'''
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        '''Return the lenght of the list that is representing the size of the list
        This method runs in a constant time because finding items in a list runs in constant time.'''
        return len(self.items)

    def is_empty(self):
        '''Return a boolean value describing whether or not the stack is empty
        testing for equality happens in constant time'''
        return self.items == []



my_stack = stack()
my_stack.push('apple')
my_stack.push('egg')
my_stack.push('pancake')
my_stack.is_empty()
print(my_stack.is_empty())



