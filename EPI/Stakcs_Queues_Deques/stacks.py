class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        '''Accepts an item as a paramater and appends it to the end of the list. Returns nothing.

        The runtime for this method is o(1), or constant time, because appending to end of a list happens in constant time.'''
        self.items.append(item)

my_stack = stack()
my_stack.push('apple')
my_stack.items
print(my_stack.items)